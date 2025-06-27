source : https://github.com/ucsd-progsys/liquidhaskell/tree/develop/

maybe :: v:b -> (a -> b) -> u:(Maybe a) -> {w:b | not (isJust u) => w == v}
isJust :: v:(Maybe a) -> {b:Bool | b == isJust v}
isNothing :: v:(Maybe a) -> {b:Bool | not (isJust v) == b}
fromJust :: {v:(Maybe a) | isJust v} -> a
fromMaybe :: v:a -> u:(Maybe a) -> {x:a | not (isJust u) => x == v}

Data.Either
-- Missing funcions -- 
8 

Data.Int 
-- Missing functions--
No functions defined in the standard library

Data.Bool


Data.Tuple
fst :: {f:(x:(a,b) -> {v:a | v = (fst x)}) | f == fst }
snd :: {f:(x:(a,b) -> {v:b | v = (snd x)}) | f == snd }
--add more--

--not present in the Hoogle
Data.Text.Fusion
module spec Data.Text.Fusion.Common where

measure slen :: Data.Text.Fusion.Internal.Stream a
             -> GHC.Types.Int

cons :: GHC.Types.Char
     -> s:Data.Text.Fusion.Internal.Stream Char
     -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) = (1 + (slen s))}

snoc :: s:Data.Text.Fusion.Internal.Stream Char
     -> GHC.Types.Char
     -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) = (1 + (slen s))}

compareLengthI :: s:Data.Text.Fusion.Internal.Stream Char
               -> l:GHC.Types.Int
               -> {v:GHC.Types.Ordering | ((v = GHC.Types.EQ) <=> ((slen s) = l))}

isSingleton :: s:Data.Text.Fusion.Internal.Stream Char
            -> {v:GHC.Types.Bool | (v <=> ((slen s) = 1))}

singleton   :: GHC.Types.Char
            -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) = 1}

streamList   :: l:[a]
             -> {v:Data.Text.Fusion.Internal.Stream a | (slen v) = (len l)}

unstreamList :: s:Data.Text.Fusion.Internal.Stream a
             -> {v:[a] | (len v) = (slen s)}

map :: (GHC.Types.Char -> GHC.Types.Char)
    -> s:Data.Text.Fusion.Internal.Stream Char
    -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) = (slen s)}

filter :: (GHC.Types.Char -> GHC.Types.Bool)
       -> s:Data.Text.Fusion.Internal.Stream Char
       -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) <= (slen s)}

intersperse :: GHC.Types.Char
            -> s:Data.Text.Fusion.Internal.Stream Char
            -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) > (slen s)}

replicateCharI :: l:GHC.Types.Int
               -> GHC.Types.Char
               -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) = l}

toCaseFold :: s:Data.Text.Fusion.Internal.Stream Char
           -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) >= (slen s)}

toUpper    :: s:Data.Text.Fusion.Internal.Stream Char
           -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) >= (slen s)}
toLower    :: s:Data.Text.Fusion.Internal.Stream Char
           -> {v:Data.Text.Fusion.Internal.Stream Char | (slen v) >= (slen s)}


Data.ByteString

module spec Data.ByteString.Lazy where

assume empty :: { bs : Data.ByteString.Lazy.ByteString | bllen bs == 0 }

assume singleton
    :: Char -> { bs : Data.ByteString.Lazy.ByteString | bllen bs == 1 }

assume pack
    :: w8s : [Char]
    -> { bs : Data.ByteString.ByteString | bllen bs == len w8s }

assume unpack
    :: bs : Data.ByteString.Lazy.ByteString
    -> { w8s : [Char] | len w8s == bllen bs }

assume fromStrict
    :: i : Data.ByteString.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bslen i }

assume toStrict
    :: i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.ByteString | bslen o == bllen i }

assume fromChunks
    :: i : [Data.ByteString.ByteString]
    -> { o : Data.ByteString.Lazy.ByteString | len i == 0 <=> bllen o == 0 }

assume toChunks
    :: i : Data.ByteString.Lazy.ByteString
    -> { os : [{ o : Data.ByteString.ByteString | bslen o <= bllen i}] | len os == 0 <=> bllen i == 0 }

assume cons
    :: Char
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i + 1 }

assume snoc
    :: i : Data.ByteString.Lazy.ByteString
    -> Char
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i + 1 }

assume append
    :: l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen l + bllen r }

head
    :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

assume uncons
    :: i : Data.ByteString.Lazy.ByteString
    -> Maybe (Char, { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i - 1 })

assume unsnoc
    :: i : Data.ByteString.Lazy.ByteString
    -> Maybe ({ o : Data.ByteString.Lazy.ByteString | bllen o == bllen i - 1 }, Char)

last
    :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

tail
    :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

init
    :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

assume null
    :: bs : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | b <=> bllen bs == 0 }

assume length
    :: bs : Data.ByteString.Lazy.ByteString -> { n : Data.Int.Int64 | bllen bs == n }

assume map
    :: (Char -> Char)
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume reverse
    :: i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume intersperse
    :: Char
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | (bllen i == 0 <=> bllen o == 0) && (1 <= bllen i <=> bllen o == 2 * bllen i - 1) }

assume intercalate
    :: l : Data.ByteString.Lazy.ByteString
    -> rs : [Data.ByteString.Lazy.ByteString]
    -> { o : Data.ByteString.Lazy.ByteString | len rs == 0 ==> bllen o == 0 }

assume transpose
    :: is : [Data.ByteString.Lazy.ByteString]
    -> { os : [{ bs : Data.ByteString.Lazy.ByteString | bllen bs <= len is }] | len is == 0 ==> len os == 0}

foldl1
    :: (Char -> Char -> Char)
    -> { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

foldl1'
    :: (Char -> Char -> Char)
    -> { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

foldr1
    :: (Char -> Char -> Char)
    -> { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

foldr1'
    :: (Char -> Char -> Char)
    -> { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs }
    -> Char

assume concat
    :: is : [Data.ByteString.Lazy.ByteString]
    -> { o : Data.ByteString.Lazy.ByteString | len is == 0 ==> bllen o }

assume concatMap
    :: (Char -> Data.ByteString.Lazy.ByteString)
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen i == 0 ==> bllen o == 0 }

assume any :: (Char -> GHC.Types.Bool)
    -> bs : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen bs == 0 ==> not b }

assume all :: (Char -> GHC.Types.Bool)
    -> bs : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen bs == 0 ==> b }

maximum :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs } -> Char

minimum :: { bs : Data.ByteString.Lazy.ByteString | 1 <= bllen bs } -> Char

assume scanl
    :: (Char -> Char -> Char)
    -> Char
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume scanl1
    :: (Char -> Char -> Char)
    -> i : { i : Data.ByteString.Lazy.ByteString | 1 <= bllen i }
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume scanr
    :: (Char -> Char -> Char)
    -> Char
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume scanr1
    :: (Char -> Char -> Char)
    -> i : { i : Data.ByteString.Lazy.ByteString | 1 <= bllen i }
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume mapAccumL
    :: (acc -> Char -> (acc, Char))
    -> acc
    -> i : Data.ByteString.Lazy.ByteString
    -> (acc, { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i })

assume mapAccumR
    :: (acc -> Char -> (acc, Char))
    -> acc
    -> i : Data.ByteString.Lazy.ByteString
    -> (acc, { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i })

assume replicate
    :: n : Data.Int.Int64
    -> Char
    -> { bs : Data.ByteString.Lazy.ByteString | bllen bs == n }

assume unfoldrN
    :: n : Int
    -> (a -> Maybe (Char, a))
    -> a
    -> ({ bs : Data.ByteString.Lazy.ByteString | bllen bs <= n }, Maybe a)

assume take
    :: n : Data.Int.Int64
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | (n <= 0 ==> bllen o == 0) &&
                                               ((0 <= n && n <= bllen i) <=> bllen o == n) &&
                                               (bllen i <= n <=> bllen o = bllen i) }

assume drop
    :: n : Data.Int.Int64
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | (n <= 0 <=> bllen o == bllen i) &&
                                               ((0 <= n && n <= bllen i) <=> bllen o == bllen i - n) &&
                                               (bllen i <= n <=> bllen o == 0) }

assume splitAt
    :: n : Data.Int.Int64
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | (n <= 0 <=> bllen l == 0) &&
                                                 ((0 <= n && n <= bllen i) <=> bllen l == n) &&
                                                 (bllen i <= n <=> bllen l == bllen i) }
       , { r : Data.ByteString.Lazy.ByteString | (n <= 0 <=> bllen r == bllen i) &&
                                                 ((0 <= n && n <= bllen i) <=> bllen r == bllen i - n) &&
                                                 (bllen i <= n <=> bllen r == 0) }
       )

assume takeWhile
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }

assume dropWhile
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }

assume span
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l <= bllen i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r <= bllen i }
       )

assume spanEnd
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l <= bllen i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r <= bllen i }
       )

assume break
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l <= bllen i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r <= bllen i }
       )

assume breakEnd
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l <= bllen i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r <= bllen i }
       )
assume group
    :: i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | 1 <= bllen o && bllen o <= bllen i }]

assume groupBy
    :: (Char -> Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | 1 <= bllen o && bllen o <= bllen i }]

assume inits
    :: i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume tails
    :: i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume split
    :: Char
    -> i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume splitWith
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume lines
    :: i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume words
    :: i : Data.ByteString.Lazy.ByteString
    -> [{ o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }]

assume unlines
    :: is : [Data.ByteString.Lazy.ByteString]
    -> { o : Data.ByteString.Lazy.ByteString | (len is == 0 <=> bllen o == 0) && bllen o >= len is }

assume unwords
    :: is : [Data.ByteString.Lazy.ByteString]
    -> { o : Data.ByteString.Lazy.ByteString | (len is == 0 ==> bllen o == 0) && (1 <= len is ==> bllen o >= len is - 1) }

assume isPrefixOf
    :: l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen l >= bllen r ==> not b }

assume isSuffixOf
    :: l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen l >= bllen r ==> not b }

assume isInfixOf
    :: l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen l >= bllen r ==> not b }

assume breakSubstring
    :: il : Data.ByteString.Lazy.ByteString
    -> ir : Data.ByteString.Lazy.ByteString
    -> ( { ol : Data.ByteString.Lazy.ByteString | bllen ol <= bllen ir && (bllen il > bllen ir ==> bllen ol == bllen ir)}
       , { or : Data.ByteString.Lazy.ByteString | bllen or <= bllen ir && (bllen il > bllen ir ==> bllen or == 0) }
       )

assume elem
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen b == 0 ==> not b }

assume notElem
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> { b : GHC.Types.Bool | bllen b == 0 ==> b }

assume find
    :: (Char -> GHC.Types.Bool)
    -> bs : Data.ByteString.Lazy.ByteString
    -> Maybe { w8 : Char | bllen bs /= 0 }

assume filter
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o <= bllen i }

assume partition
    :: (Char -> GHC.Types.Bool)
    -> i : Data.ByteString.Lazy.ByteString
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l <= bllen i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r <= bllen i }
       )

index
    :: bs : Data.ByteString.Lazy.ByteString
    -> { n : Data.Int.Int64 | 0 <= n && n < bllen bs }
    -> Char

assume elemIndex
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> Maybe { n : Data.Int.Int64 | 0 <= n && n < bllen bs }

assume elemIndices
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> [{ n : Data.Int.Int64 | 0 <= n && n < bllen bs }]

assume elemIndexEnd
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> Maybe { n : Data.Int.Int64 | 0 <= n && n < bllen bs }

assume findIndex
    :: (Char -> GHC.Types.Bool)
    -> bs : Data.ByteString.Lazy.ByteString
    -> Maybe { n : Data.Int.Int64 | 0 <= n && n < bllen bs }

assume findIndices
    :: (Char -> GHC.Types.Bool)
    -> bs : Data.ByteString.Lazy.ByteString
    -> [{ n : Data.Int.Int64 | 0 <= n && n < bllen bs }]

assume count
    :: Char
    -> bs : Data.ByteString.Lazy.ByteString
    -> { n : Data.Int.Int64 | 0 <= n && n < bllen bs }

assume zip
    :: l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { o : [(Char, Char)] | len o <= bllen l && len o <= bllen r }

assume zipWith
    :: (Char -> Char -> a)
    -> l : Data.ByteString.Lazy.ByteString
    -> r : Data.ByteString.Lazy.ByteString
    -> { o : [a] | len o <= bllen l && len o <= bllen r }

assume unzip
    :: i : [(Char, Char)]
    -> ( { l : Data.ByteString.Lazy.ByteString | bllen l == len i }
       , { r : Data.ByteString.Lazy.ByteString | bllen r == len i }
       )

assume sort
    :: i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume readInt
    :: i : Data.ByteString.Lazy.ByteString
    -> Maybe { p : (Int, { o : Data.ByteString.Lazy.ByteString | bllen o < bllen i}) | bllen i /= 0 }

assume readInteger
    :: i : Data.ByteString.Lazy.ByteString
    -> Maybe { p : (Integer, { o : Data.ByteString.Lazy.ByteString | bllen o < bllen i}) | bllen i /= 0 }

assume copy
    :: i : Data.ByteString.Lazy.ByteString
    -> { o : Data.ByteString.Lazy.ByteString | bllen o == bllen i }

assume hGet
    :: System.IO.Handle
    -> n : { n : Int | 0 <= n }
    -> IO { bs : Data.ByteString.Lazy.ByteString | bllen bs == n || bllen bs == 0 }

assume hGetNonBlocking
    :: System.IO.Handle
    -> n : { n : Int | 0 <= n }
    -> IO { bs : Data.ByteString.Lazy.ByteString | bllen bs <= n }


Data.Time.Calendar
module spec Data.Time.Calendar where

type NumericMonth = { x:Nat | 0 < x && x <= 12 }

type NumericDayOfMonth = { x:Nat | 0 < x && x <= 31 }

fromGregorian :: Integer -> NumericMonth -> NumericDayOfMonth -> Day

toGregorian :: Day -> (Integer,NumericMonth,NumericDayOfMonth)

gregorianMonthLength :: Integer -> NumericMonth -> { x:Nat | 28 <= x && x <= 31 }



Data.Foldable 
module spec Data.Foldable where

import GHC.Base

length :: Data.Foldable.Foldable f => forall a. xs:f a -> {v:Nat | v = len xs}
null :: v:_ -> {b:Bool | (b <=> len v = 0) && (not b <=> len v > 0)}

-- Missing functions--



Data.Map 

module spec Data.Map where

embed Data.Map.Map as Map_t

---------------------------------------------------------------------------------------
-- | Logical Map Operators: Interpreted "natively" by the SMT solver ------------------
---------------------------------------------------------------------------------------

measure Map_select :: forall k v. Data.Map.Map k v -> k -> v

measure Map_store  :: forall k v. Data.Map.Map k v -> k -> v -> Data.Map.Map k v


insert :: Ord k => k:k -> v:v -> m:Data.Map.Map k v -> {n:Data.Map.Map k v | n = Map_store m k v}

lookup :: Ord k => k:k -> m:Data.Map.Map k v -> Maybe {v:v | v = Map_select m k}

(!)    :: Ord k => m:Data.Map.Map k v -> k:k -> {v:v | v = Map_select m k}


-- Missing Functions ---



Data.set


module spec Data.Set where

embed Data.Set.Internal.Set as Set_Set

//  ----------------------------------------------------------------------------------------------
//  -- | Logical Set Operators: Interpreted "natively" by the SMT solver -------------------------
//  ----------------------------------------------------------------------------------------------


//  union
measure Set_cup  :: (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a)

//  intersection
measure Set_cap  :: (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a)

//  difference
measure Set_dif   :: (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a)

//  singleton
measure Set_sng   :: a -> (Data.Set.Internal.Set a)

//  emptiness test
measure Set_emp   :: (Data.Set.Internal.Set a) -> GHC.Types.Bool

//  empty set
measure Set_empty :: forall a. GHC.Types.Int -> (Data.Set.Internal.Set a)

//  membership test
measure Set_mem  :: a -> (Data.Set.Internal.Set a) -> GHC.Types.Bool

//  inclusion test
measure Set_sub  :: (Data.Set.Internal.Set a) -> (Data.Set.Internal.Set a) -> GHC.Types.Bool

//  ---------------------------------------------------------------------------------------------
//  -- | Refined Types for Data.Set Operations --------------------------------------------------
//  ---------------------------------------------------------------------------------------------

isSubsetOf    :: (GHC.Classes.Ord a) => x:(Data.Set.Internal.Set a) -> y:(Data.Set.Internal.Set a) -> {v:GHC.Types.Bool | v <=> Set_sub x y}
member        :: (GHC.Classes.Ord a) => x:a -> xs:(Data.Set.Internal.Set a) -> {v:GHC.Types.Bool | v <=> Set_mem x xs}
null          :: xs:(Data.Set.Internal.Set a) -> {v:GHC.Types.Bool | v <=> Set_emp xs}

empty         :: {v:(Data.Set.Internal.Set a) | Set_emp v}
singleton     :: x:a -> {v:(Data.Set.Internal.Set a) | v = (Set_sng x)}
insert        :: (GHC.Classes.Ord a) => x:a -> xs:(Data.Set.Internal.Set a) -> {v:(Data.Set.Internal.Set a) | v = Set_cup xs (Set_sng x)}
delete        :: (GHC.Classes.Ord a) => x:a -> xs:(Data.Set.Internal.Set a) -> {v:(Data.Set.Internal.Set a) | v = Set_dif xs (Set_sng x)}

union         :: GHC.Classes.Ord a => xs:(Data.Set.Internal.Set a) -> ys:(Data.Set.Internal.Set a) -> {v:(Data.Set.Internal.Set a) | v = Set_cup xs ys}
intersection  :: GHC.Classes.Ord a => xs:(Data.Set.Internal.Set a) -> ys:(Data.Set.Internal.Set a) -> {v:(Data.Set.Internal.Set a) | v = Set_cap xs ys}
difference    :: GHC.Classes.Ord a => xs:(Data.Set.Internal.Set a) -> ys:(Data.Set.Internal.Set a) -> {v:(Data.Set.Internal.Set a) | v = Set_dif xs ys}

fromList :: GHC.Classes.Ord a => xs:[a] -> {v:Data.Set.Internal.Set a | v = listElts xs}

//  ---------------------------------------------------------------------------------------------
//  -- | The set of elements in a list ----------------------------------------------------------
//  ---------------------------------------------------------------------------------------------

measure listElts :: [a] -> (Data.Set.Internal.Set a)
  listElts []     = {v | (Set_emp v)}
  listElts (x:xs) = {v | v = Set_cup (Set_sng x) (listElts xs) }



Data.Text

module spec Data.Text where

import Data.String

measure tlen :: Data.Text.Text -> { n : Int | 0 <= n }

invariant { t : Data.Text.Text  | 0 <= tlen t }

invariant { t : Data.Text.Text | tlen t == stringlen t }

empty :: { t : Data.Text.Text | tlen t == 0 }

singleton :: _ -> { t : Data.Text.Text | tlen t == 1 }

pack :: str : [_]
     -> { t : Data.Text.Text | tlen t == len str }

unpack :: t : Data.Text.Text
       -> { str : [_] | len str == tlen t }

cons :: _
     -> i : Data.Text.Text
     -> { o : Data.Text.Text | tlen o == tlen i + 1 }

snoc :: i : Data.Text.Text
     -> _
     -> { o : Data.Text.Text | tlen o == tlen i + 1 }

append :: l : Data.Text.Text
       -> r : Data.Text.Text
       -> { o : Data.Text.Text | tlen o == tlen l + tlen r }

head :: { t : Data.Text.Text | 1 <= tlen t } -> _

unsnoc :: i:Data.Text.Text
       -> (Maybe ({ o : Data.Text.Text | tlen o == tlen i - 1 }, _))

last :: { t : Data.Text.Text | 1 <= tlen t } -> _

tail :: { t : Data.Text.Text | 1 <= tlen t } -> _

init
  :: {i:Data.Text.Text | 1 <= tlen i }
  -> {o:Data.Text.Text | tlen o == tlen i - 1 }

null
  :: t : Data.Text.Text
  -> { b : GHC.Types.Bool | b <=> tlen t == 0 }

length :: t : Data.Text.Text -> { n : Int | tlen t == n }

map
  :: (_ -> _)
  -> i : Data.Text.Text
  -> { o : Data.Text.Text | tlen o == tlen i }

reverse
  :: i : Data.Text.Text
  -> { o : Data.Text.Text | tlen o == tlen i }

intersperse
  :: _
  -> i : Data.Text.Text
  -> { o : Data.Text.Text | (tlen i == 0 <=> tlen o == 0) && (1 <= tlen i <=> tlen o == 2 * tlen i - 1) }

intercalate
  :: l : Data.Text.Text
  -> rs : [Data.Text.Text]
  -> { o : Data.Text.Text | len rs == 0 ==> tlen o == 0 }

transpose
  :: is : [Data.Text.Text]
  -> { os : [{ t : Data.Text.Text | tlen t <= len is }] | len is == 0 ==> len os == 0}

foldl1
  :: (_ -> _ -> _)
  -> { t : Data.Text.Text | 1 <= tlen t }
  -> _

foldl1'
  :: (_ -> _ -> _)
  -> { t : Data.Text.Text | 1 <= tlen t }
  -> _

foldr1
  :: (_ -> _ -> _)
  -> { t : Data.Text.Text | 1 <= tlen t }
  -> _

concat
  :: is : [Data.Text.Text]
  -> { o : Data.Text.Text | (len is == 0) ==> (tlen o == 0) }

concatMap
  :: (_ -> Data.Text.Text)
  -> i : Data.Text.Text
  -> { o : Data.Text.Text | tlen i == 0 ==> tlen o == 0 }

any
  :: (_ -> GHC.Types.Bool)
  -> t : Data.Text.Text
  -> { b : GHC.Types.Bool | tlen t == 0 ==> not b }

all
  :: (_ -> GHC.Types.Bool)
  -> t : Data.Text.Text
  -> { b : GHC.Types.Bool | tlen t == 0 ==> b }

maximum :: { t : Data.Text.Text | 1 <= tlen t } -> _

minimum :: { t : Data.Text.Text | 1 <= tlen t } -> _

scanl :: (_ -> _ -> _)
      -> _
      -> i : Data.Text.Text
      -> { o : Data.Text.Text | tlen o == tlen i }

scanl1 :: (_ -> _ -> _)
       -> i : { i : Data.Text.Text | 1 <= tlen i }
       -> { o : Data.Text.Text | tlen o == tlen i }

scanr
    :: (_ -> _ -> _)
    -> _
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | tlen o == tlen i }

scanr1
    :: (_ -> _ -> _)
    -> i : { i : Data.Text.Text | 1 <= tlen i }
    -> { o : Data.Text.Text | tlen o == tlen i }

mapAccumL
    :: (acc -> _ -> (acc, _))
    -> acc
    -> i : Data.Text.Text
    -> (acc, { o : Data.Text.Text | tlen o == tlen i })

mapAccumR
    :: (acc -> _ -> (acc, _))
    -> acc
    -> i : Data.Text.Text
    -> (acc, { o : Data.Text.Text | tlen o == tlen i })

replicate
    :: n : Int
    -> _
    -> { t : Data.Text.Text | tlen t == n }

unfoldrN
    :: n : Int
    -> (a -> Maybe (_, a))
    -> a
    -> { t : Data.Text.Text | tlen t <= n }

take
    :: n : Int
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | (n <= 0 <=> tlen o == 0) &&
                                          ((0 <= n && n <= tlen i) <=> tlen o == n) &&
                                          (tlen i <= n <=> tlen o = tlen i) }

drop
    :: n : Int
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | (n <= 0 <=> tlen o == tlen i) &&
                                          ((0 <= n && n <= tlen i) <=> tlen o == tlen i - n) &&
                                          (tlen i <= n <=> tlen o == 0) }

splitAt
    :: n : Int
    -> i : Data.Text.Text
    -> ( { l : Data.Text.Text | (n <= 0 <=> tlen l == 0) &&
                                            ((0 <= n && n <= tlen i) <=> tlen l == n) &&
                                            (tlen i <= n <=> tlen l == tlen i) }
       , { r : Data.Text.Text | (n <= 0 <=> tlen r == tlen i) &&
                                            ((0 <= n && n <= tlen i) <=> tlen r == tlen i - n) &&
                                            (tlen i <= n <=> tlen r == 0) }
       )

takeWhile
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | tlen o <= tlen i }

dropWhile
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | tlen o <= tlen i }

span
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> ( { l : Data.Text.Text | tlen l <= tlen i }
       , { r : Data.Text.Text | tlen r <= tlen i }
       )

break
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> ( { l : Data.Text.Text | tlen l <= tlen i }
       , { r : Data.Text.Text | tlen r <= tlen i }
       )

group
    :: i : Data.Text.Text
    -> [{ o : Data.Text.Text | 1 <= tlen o && tlen o <= tlen i }]

groupBy
    :: (_ -> _ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> [{ o : Data.Text.Text | 1 <= tlen o && tlen o <= tlen i }]

inits
    :: i : Data.Text.Text
    -> [{ o : Data.Text.Text | tlen o <= tlen i }]

tails
    :: i : Data.Text.Text
    -> [{ o : Data.Text.Text | tlen o <= tlen i }]

split
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> [{ o : Data.Text.Text | tlen o <= tlen i }]

isPrefixOf
    :: l : Data.Text.Text
    -> r : Data.Text.Text
    -> { b : GHC.Types.Bool | tlen l >= tlen r ==> not b }

isSuffixOf
    :: l : Data.Text.Text
    -> r : Data.Text.Text
    -> { b : GHC.Types.Bool | tlen l > tlen r ==> not b }

isInfixOf
    :: l : Data.Text.Text
    -> r : Data.Text.Text
    -> { b : GHC.Types.Bool | tlen l > tlen r ==> not b }

find
    :: (_ -> GHC.Types.Bool)
    -> t : Data.Text.Text
    -> (Maybe { char : _ | tlen t /= 0 })

filter
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> { o : Data.Text.Text | tlen o <= tlen i }

partition
    :: (_ -> GHC.Types.Bool)
    -> i : Data.Text.Text
    -> ( { l : Data.Text.Text | tlen l <= tlen i }
       , { r : Data.Text.Text | tlen r <= tlen i }
       )

index :: t : Data.Text.Text -> { n : Int | 0 <= n && n < tlen t } -> _

findIndex
    :: (_ -> GHC.Types.Bool)
    -> t : Data.Text.Text
    -> (Maybe { n : Int | 0 <= n && n < tlen t })

count
    :: _
    -> t : Data.Text.Text
    -> { n : Int | 0 <= n && n < tlen t }

zip
    :: l : Data.Text.Text
    -> r : Data.Text.Text
    -> { o : [(_, _)] | len o <= tlen l && len o <= tlen r }

zipWith
    :: (_ -> _ -> Char)
    -> l : Data.Text.Text
    -> r : Data.Text.Text
    -> { o : Text | tlen o <= tlen l && tlen o <= tlen r }

copy
    :: i : Data.Text.Text
    -> { o : Data.Text.Text | tlen o == tlen i }

uncons
    :: i : Data.Text.Text
    -> (Maybe (_, { o : Data.Text.Text | tlen o == tlen i - 1 }))




Data.Vector


module spec Data.Vector where

import GHC.Base

data variance Data.Vector.Vector covariant


measure vlen    :: forall a. (Data.Vector.Vector a) -> Int

invariant       {v: Data.Vector.Vector a | 0 <= vlen v } 

!           :: forall a. x:(Data.Vector.Vector a) -> vec:{v:Nat | v < vlen x } -> a 

unsafeIndex :: forall a. x:(Data.Vector.Vector a) -> vec:{v:Nat | v < vlen x } -> a 

fromList  :: forall a. x:[a] -> {v: Data.Vector.Vector a  | vlen v = len x }

length    :: forall a. x:(Data.Vector.Vector a) -> {v : Nat | v = vlen x }

replicate :: n:Nat -> a -> {v:Data.Vector.Vector a | vlen v = n} 

imap :: (Nat -> a -> b) -> x:(Data.Vector.Vector a) -> {y:Data.Vector.Vector b | vlen y = vlen x }

map :: (a -> b) -> x:(Data.Vector.Vector a) -> {y:Data.Vector.Vector b | vlen y = vlen x }

head :: forall a. {xs: Data.Vector.Vector a | vlen xs > 0} -> a 




GHC.Classes
module spec GHC.Classes where

import GHC.Types

not     :: x:GHC.Types.Bool -> {v:GHC.Types.Bool | ((v) <=> ~(x))}
(&&)    :: x:GHC.Types.Bool -> y:GHC.Types.Bool
        -> {v:GHC.Types.Bool | ((v) <=> ((x) && (y)))}
(||)    :: x:GHC.Types.Bool -> y:GHC.Types.Bool
        -> {v:GHC.Types.Bool | ((v) <=> ((x) || (y)))}
(==)    :: (GHC.Classes.Eq  a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x = y)}
(/=)    :: (GHC.Classes.Eq  a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x != y)}
(>)     :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x > y)}
(>=)    :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x >= y)}
(<)     :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x < y)}
(<=)    :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x <= y)}

compare :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Ordering | (((v = GHC.Types.EQ) <=> (x = y)) &&
                                    ((v = GHC.Types.LT) <=> (x < y)) &&
                                    ((v = GHC.Types.GT) <=> (x > y))) }

max :: (GHC.Classes.Ord a) => x:a -> y:a -> {v:a | v = (if x > y then x else y) }
min :: (GHC.Classes.Ord a) => x:a -> y:a -> {v:a | v = (if x < y then x else y) }



GHC.List 
module spec GHC.List where 

head         :: xs:{v: [a] | len v > 0} -> {v:a | v = head xs}
tail         :: xs:{v: [a] | len v > 0} -> {v: [a] | len(v) = (len(xs) - 1) && v = tail xs}

last         :: xs:{v: [a] | len v > 0} -> a
init         :: xs:{v: [a] | len v > 0} -> {v: [a] | len(v) = len(xs) - 1}
null         :: xs:[a] -> {v: GHC.Types.Bool | ((v) <=> len(xs) = 0) }
length       :: xs:[a] -> {v: GHC.Types.Int | v = len(xs)}
filter       :: (a -> GHC.Types.Bool) -> xs:[a] -> {v: [a] | len(v) <= len(xs)}
scanl        :: (a -> b -> a) -> a -> xs:[b] -> {v: [a] | len(v) = 1 + len(xs) }
scanl1       :: (a -> a -> a) -> xs:{v: [a] | len(v) > 0} -> {v: [a] | len(v) = len(xs) }
foldr1       :: (a -> a -> a) -> xs:{v: [a] | len(v) > 0} -> a
scanr        :: (a -> b -> b) -> b -> xs:[a] -> {v: [b] | len(v) = 1 + len(xs) }
scanr1       :: (a -> a -> a) -> xs:{v: [a] | len(v) > 0} -> {v: [a] | len(v) = len(xs) }

lazy GHC.List.iterate
iterate :: (a -> a) -> a -> [a]

repeat :: a -> [a]
lazy GHC.List.repeat

replicate    :: n:Nat -> x:a -> {v: [{v:a | v = x}] | len(v) = n}

cycle        :: {v: [a] | len(v) > 0 } -> [a]
lazy cycle

takeWhile    :: (a -> GHC.Types.Bool) -> xs:[a] -> {v: [a] | len(v) <= len(xs)}
dropWhile    :: (a -> GHC.Types.Bool) -> xs:[a] -> {v: [a] | len(v) <= len(xs)}

take :: n:GHC.Types.Int
     -> xs:[a]
     -> {v:[a] | if n >= 0 then (len v = (if (len xs) < n then (len xs) else n)) else (len v = 0)}
drop :: n:GHC.Types.Int
     -> xs:[a]
     -> {v:[a] | (if (n >= 0) then (len(v) = (if (len(xs) < n) then 0 else len(xs) - n)) else ((len v) = (len xs)))}

splitAt :: n:_ -> x:[a] -> ({v:[a] | (if (n >= 0) then (if (len x) < n then (len v) = (len x) else (len v) = n) else 
                                                            ((len v) = 0))},[a])<{\x1 x2 -> (len x2) = (len x) - (len x1)}>
span    :: (a -> GHC.Types.Bool) 
        -> xs:[a] 
        -> ({v:[a]|((len v)<=(len xs))}, {v:[a]|((len v)<=(len xs))})

break :: (a -> GHC.Types.Bool) -> xs:[a] -> ([a],[a])<{\x y -> (len xs) = (len x) + (len y)}>

          :: xs:[a] -> {v: [a] | len(v) = len(xs)}

include <len.hquals>

GHC.List.!!         :: xs:[a] -> {v: _ | ((0 <= v) && (v < len(xs)))} -> a


zip :: xs : [a] -> ys:[b]
            -> {v : [(a, b)] | ((((len v) <= (len xs)) && ((len v) <= (len ys)))
            && (((len xs) = (len ys)) => ((len v) = (len xs))) )}

zipWith :: (a -> b -> c) 
        -> xs : [a] -> ys:[b] 
        -> {v : [c] | (((len v) <= (len xs)) && ((len v) <= (len ys)))}

errorEmptyList :: {v: _ | false} -> a


GHC.Num

module spec GHC.Num where

// embed GHC.Integer.Type.Integer as int 

GHC.Num.fromInteger :: (GHC.Num.Num a) => x:_ -> {v:a | v = x }

GHC.Num.negate :: (GHC.Num.Num a)
               => x:a
               -> {v:a | v = -x}


GHC.Ptr (Only Simple pointers)

module spec GHC.Ptr where

measure pbase     :: GHC.Ptr.Ptr a -> GHC.Types.Int
measure plen      :: GHC.Ptr.Ptr a -> GHC.Types.Int
measure isNullPtr :: GHC.Ptr.Ptr a -> Bool 

invariant {v:Foreign.Ptr.Ptr a | 0 <= plen  v }
invariant {v:Foreign.Ptr.Ptr a | 0 <= pbase v }

type PtrN a N = {v: PtrV a        | plen v == N }
type PtrV a   = {v: GHC.Ptr.Ptr a | 0 <= plen v }

GHC.Ptr.castPtr :: p:(PtrV a) -> (PtrN b (plen p))

GHC.Ptr.plusPtr :: base:(PtrV a)
                -> off:{v:GHC.Types.Int | v <= plen base }
                -> {v:(PtrV b) | pbase v = pbase base && plen v = plen base - off}

GHC.Ptr.minusPtr :: q:(PtrV a)
                 -> p:{v:(PtrV b) | pbase v == pbase q && plen v >= plen q}
                 -> {v:Nat | v == plen p - plen q}

measure deref     :: GHC.Ptr.Ptr a -> a


GHC.Read 

module spec GHC.Read where

type ParsedString XS =  {v:_ | (if ((len XS) > 0) then ((len v) < (len XS)) else ((len v) = 0))}

GHC.Read.lex :: xs:_ -> [((ParsedString xs), (ParsedString xs))]


GHC.Real 

module spec GHC.Real where

(GHC.Real.^) :: (GHC.Num.Num a, GHC.Real.Integral b) => a:a -> n:b -> {v:a | v == 0 <=> a == 0 }

GHC.Real.fromIntegral    :: (GHC.Real.Integral a, GHC.Num.Num b) => x:a -> {v:b|v=x}

class (GHC.Num.Num a) => GHC.Real.Fractional a where
  (GHC.Real./)   :: x:a -> y:{v:a | v /= 0} -> {v:a | v == x / y}
  GHC.Real.recip :: a -> a
  GHC.Real.fromRational :: GHC.Real.Ratio Integer -> a

class (GHC.Real.Real a, GHC.Enum.Enum a) => GHC.Real.Integral a where
  GHC.Real.quot :: x:a -> y:{v:a | v /= 0} -> {v:a | (v = (x / y)) &&
                                                     ((x >= 0 && y >= 0) => v >= 0) &&
                                                     ((x >= 0 && y >= 1) => v <= x) }
  GHC.Real.rem :: x:a -> y:{v:a | v /= 0} -> {v:a | ((v >= 0) && (v < y))}
  GHC.Real.mod :: x:a -> y:{v:a | v /= 0} -> {v:a | v = x mod y && ((0 <= x && 0 < y) => (0 <= v && v < y))}

  GHC.Real.div :: x:a -> y:{v:a | v /= 0} -> {v:a | (v = (x / y)) &&
                                                    ((x >= 0 && y >= 0) => v >= 0) &&
                                                    ((x >= 0 && y >= 1) => v <= x) && 
                                                    ((1 < y)            => v < x ) && 
                                                    ((y >= 1)           => v <= x)  
                                                    }
  GHC.Real.quotRem :: x:a -> y:{v:a | v /= 0} -> ( {v:a | (v = (x / y)) &&
                                                          ((x >= 0 && y >= 0) => v >= 0) &&
                                                          ((x >= 0 && y >= 1) => v <= x)}
                                                 , {v:a | ((v >= 0) && (v < y))})
  GHC.Real.divMod :: x:a -> y:{v:a | v /= 0} -> ( {v:a | (v = (x / y)) &&
                                                         ((x >= 0 && y >= 0) => v >= 0) &&
                                                         ((x >= 0 && y >= 1) => v <= x) }
                                                , {v:a | v = x mod y && ((0 <= x && 0 < y) => (0 <= v && v < y))}
                                                )
  GHC.Real.toInteger :: x:a -> {v:GHC.Integer.Type.Integer | v = x}

//  fixpoint can't handle (x mod y), only (x mod c) so we need to be more clever here
//  mod :: x:a -> y:a -> {v:a | v = (x mod y) }
