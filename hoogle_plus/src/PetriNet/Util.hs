{-# LANGUAGE FlexibleContexts #-} 
module PetriNet.Util where

import Types.Type
import Types.Common
import Types.Solver
import Types.Abstract
import Types.Experiments
import Types.Environment
import Types.Program
import Types.Encoder
import Types.IOFormat
import Types.Filtering (AssociativeExamples)
import Types.CheckMonad
import Types.TypeChecker (Checker)
import Types.InfConstraint (wildcardPrefix)
import qualified Types.TypeChecker as Checker
import Synquid.Program
import Synquid.Logic hiding (varName)
import Synquid.Type
import Synquid.Pretty
import Synquid.Util
import HooglePlus.Utils
import Database.Util (tyclassArgBase, hoPostfix)

import Control.Concurrent.Chan
import Control.Lens
import Control.Monad.State
import Control.Monad.Extra
import Control.Monad.ST (runST, ST)
import Debug.Trace
import Data.Array.ST (STArray, readArray, writeArray, newListArray, getElems)
import Data.Hashable
import Data.List.Extra
import Data.Maybe
import qualified Data.Text as Text
import Data.Map (Map)
import Data.Set (Set)
import qualified Data.Map as Map
import qualified Data.Set as Set
import Data.HashMap.Strict (HashMap)
import qualified Data.HashMap.Strict as HashMap
import Text.Pretty.Simple
import Text.Printf
import qualified Hoogle as Hoogle

getExperiment exp = gets $ view (searchParams . exp)

-------------------------------------------------------------------------------
-- | helper functions
-------------------------------------------------------------------------------
writeLog :: (CheckMonad (t m), MonadIO (t m), MonadIO m) => Int -> String -> Doc -> t m ()
writeLog level tag msg = do
    mesgChan <- getMessageChan
    liftIO $ writeChan mesgChan (MesgLog level tag $ show $ plain msg)
    -- if level <= 1 then trace (printf "[%s]: %s\n" tag (show $ plain msg)) $ return () else return ()

multiPermutation len elmts | len == 0 = [[]]
multiPermutation len elmts | len == 1 = [[e] | e <- elmts]
multiPermutation len elmts            = nubSpence [ l:r | l <- elmts, r <- multiPermutation (len - 1) elmts]

-- Thanks, this only helps when you get >100 elements, otherwise, use nubOrd:
-- https://github.com/AndreasPK/nubBench/blob/038bc644f32aaa47035484b4384a4aaf5b78320c/app/Main.hs
nubSpence :: (Hashable a, Eq a) => [a] -> [a]
nubSpence l = runST $ do
  arr <- mr
  forM_ l $ \j -> do
    let index = (hash j) `mod` 255
    current <- readArray arr index
    let new = if j `elem` current then current else j : current
    writeArray arr index new
  join <$> getElems arr
    where
      mr :: ST s (STArray s Int [a])
      mr = newListArray (0, 255) (replicate 256 [])

listDiff left right = Set.toList $ (Set.fromList left) `Set.difference` (Set.fromList right)


var2any env t@(ScalarT (TypeVarT _ id) _) | isBound env id = t
var2any env t@(ScalarT (TypeVarT _ id) _) = AnyT
var2any env (ScalarT (DatatypeT id args l) r) = ScalarT (DatatypeT id (map (var2any env) args) l) r
var2any env (FunctionT x tArg tRet) = FunctionT x (var2any env tArg) (var2any env tRet)

freshId :: (CheckMonad (t m), MonadIO m) => [Id] -> Id -> t m Id
freshId bounds prefix = do
    indices <- getNameCounter
    let idx = Map.findWithDefault 0 prefix indices
    setNameCounter $ Map.insert prefix (idx+1) indices
    let v = prefix ++ show idx
    if v `elem` bounds then freshId bounds prefix else return v

-- | Replace all bound type variables with fresh free variables
freshType :: (CheckMonad (t m), MonadIO m) => [Id] -> RSchema -> t m RType
freshType bounds t = freshType' Map.empty [] t
  where
    freshType' subst constraints (ForallT a sch) = do
        a' <- freshId bounds "tau"
        let v = if head a == wildcardPrefix then wildcardPrefix:a' else a'
        freshType' (Map.insert a (vart v ftrue) subst) (v:constraints) sch
    freshType' subst constraints (Monotype t) = return (typeSubstitute subst t)

findSymbol :: (CheckMonad (t m), MonadIO (t m), MonadIO m) => Environment -> Id -> t m RType
findSymbol env sym = do
    nameMap <- getNameMapping
    let name = fromMaybe sym (Map.lookup sym nameMap)
    let bound = env ^. boundTypeVars
    case lookupSymbol name 0 env of
        Nothing ->
            case lookupSymbol ("(" ++ name ++ ")") 0 env of
                Nothing -> do
                    setIsChecked False
                    writeLog 2 "findSymbol" $ text "cannot find symbol" <+> text name <+> text "in the current environment"
                    return AnyT
                Just sch -> freshType bound sch
        Just sch -> freshType bound sch

freshAbstract :: (CheckMonad (t m), MonadIO m) => [Id] -> AbstractSkeleton -> t m AbstractSkeleton
freshAbstract bound t = do
    (_, t') <- freshAbstract' bound Map.empty t
    return t'
  where
    freshAbstract' bound m t@(AScalar (ATypeVarT id)) | id `elem` bound = return (m, t)
    freshAbstract' bound m (AScalar (ATypeVarT id)) | id `Map.member` m =
        return (m, fromJust (Map.lookup id m))
    freshAbstract' bound m (AScalar (ATypeVarT id)) = do
        v <- freshId bound "A"
        let t = AScalar (ATypeVarT v)
        return (Map.insert id t m, AScalar (ATypeVarT v))
    freshAbstract' bound m (AScalar (ADatatypeT id args)) = do
        (m', args') <- foldM (\(accm, acct) t -> do
            (m', t') <- freshAbstract' bound accm t
            return (m', acct++[t'])) (m,[]) args
        return (m', AScalar (ADatatypeT id args'))
    freshAbstract' bound m (AFunctionT tArg tRes) = do
        (m', tArg') <- freshAbstract' bound m tArg
        (m'', tRes') <- freshAbstract' bound m' tRes
        return (m'', AFunctionT tArg' tRes')

mkConstraint :: MonadIO m => [Id] -> Id -> AbstractSkeleton -> PNSolver m UnifConstraint
mkConstraint bound v t = do
    t' <- freshAbstract bound t
    return (AScalar (ATypeVarT v), t')

groupSignatures :: MonadIO m => Map Id FunctionCode -> PNSolver m (Map FunctionCode GroupId, Map GroupId (Set Id))
groupSignatures sigs = do
    let sigsByType = Map.map Set.fromList $ groupByMap sigs
    writeLog 3 "groupSignatures" $ pretty sigsByType
    let sigLists = Map.toList sigsByType
    signatureGroups <- flip zip sigLists <$> mapM (\_ -> freshId [] "gm") [() | _ <- sigLists]
    let dupes = [Set.size $ snd $ snd x | x <- signatureGroups, Set.size (snd $ snd x) > 1]
    let allIds = [Set.size $ snd $ snd x | x <- signatureGroups]
    writeLog 3 "groupSignatures" $ text $ printf "%d class; %d equiv; %d total"
        (length sigLists) (sum dupes) (Map.size sigs)
    let groupMap = Map.fromList $ map (\(gid, (_, ids)) -> (gid, ids)) signatureGroups
    let t2g = Map.fromList $ map (\(gid, (aty, _)) -> (aty, gid)) signatureGroups
    -- write out the info.
    mesgChan <- gets $ view messageChan
    modify $ over (statistics . solverStats . duplicateSymbols) (++ [(length sigLists, sum dupes, sum $ map length $ sigLists)])
    return (t2g, groupMap)

removeLast :: Char -> String -> String
removeLast c1 = snd . remLast
  where
    remLast :: String -> (Bool, String)
    remLast [] = (False, [])
    remLast (c2:cs) =
      case remLast cs of
        (True, cs') -> (True, c2:cs')
        (False, cs') -> if c1 == c2 then (True, []) else (False, c2:cs')

innerTextHTML :: String -> String
innerTextHTML ('<':xs) = innerTextHTML $ drop 1 $ dropWhile (/= '>') xs
innerTextHTML (x:xs) = x : innerTextHTML xs
innerTextHTML [] = []

unHTML :: String -> String
unHTML = unescapeHTML . innerTextHTML

toOutput :: Environment -> RProgram -> AssociativeExamples -> IO QueryOutput
toOutput env soln exs = do
    let symbols = Set.toList $ symbolsOf soln
    let argNames = map fst (env ^. arguments)
    let args = env ^. arguments
    let argDocs = map (\(n, ty) -> FunctionDoc n (show ty) "") args
    let symbolsWoArgs = symbols \\ argNames
    -- docs <- liftIO $ hoogleIt symbolsWoArgs
    let docs = []
    entries <- mapM mkEntry exs
    return $ QueryOutput entries "" (docs ++ argDocs)
    where
        mkEntry ((unqualSol, qualSol), ex) = do
            ex' <- mapM niceInputs ex
            let qualSol' = toHaskellSolution $ show qualSol
            let unqualSol' = toHaskellSolution $ show unqualSol
            return (ResultEntry qualSol' unqualSol' ex')
        hoogleIt syms = do
            dbPath <- Hoogle.defaultDatabaseLocation
            Hoogle.withDatabase dbPath (\db -> do
                let targets = map (head . Hoogle.searchDatabase db) syms
                let docs = map targetToDoc targets
                return docs)

        targetToDoc tg = let wholeSig = unHTML $ Hoogle.targetItem tg
                             segs = splitOn " :: " wholeSig
                             name = head segs
                             sig = unwords $ tail segs
                             doc = unHTML $ Hoogle.targetDocs tg
                          in FunctionDoc name sig doc

stripSuffix :: String -> String
stripSuffix = replaceId hoPostfix "" . removeLast '_'