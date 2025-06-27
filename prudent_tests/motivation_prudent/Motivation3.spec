
type apair;

qualifier llen : [a] :-> int;
qualifier pllen : [apair] :-> int;

qualifier lmem : [a] :-> a :-> bool;
qualifier lhd : [a] :-> a;
qualifier plhd : [apair] :-> apair;

qualifier last  : [a] :-> a;
qualifier pllast  : [apair] :-> apair;

qualifier ppr1  : apair :-> a;
qualifier ppr2  : apair :-> a;


qualifier nth : [a] :-> int :-> a;
qualifier lsnd : [a] :-> a;
qualifier pen : [a] :-> a;


ep : a;

length : (x : [a]) -> 
         State {\(h : heap). true} 
			v : {v : int | true}
		  {\(h : heap), (v : int), (h' : heap). 
			[h'= h] /\
            llen (x) = v}; 



rev : (l : [a]) -> 
      State {\(h : heap). true} 
			v :{ v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
				[h'=h] /\
            llen (v) == llen (l) /\
            lhd (v) = last (l) /\
            last (v) = lhd (l) /\
            lsnd (v) = pen (l) /\
            pen (v) = lsnd (v)

        };



compare_lengths : (x : [a]) -> (y: [a]) -> 
      State {\(h : heap). true} 
			v : {v : int | true}
		{\(h : heap), (v : int), (h' : heap). 
				[h'=h] /\
            [v = 0] <=> llen (x) == llen  (y) 
        };



compare_length_with : (x : [a]) -> (n: int) -> 
      State {\(h : heap). true} 
			v : {v : int | true}
		{\(h : heap), (v : int), (h' : heap). 
				[h'=h] /\
            [v = 0] <=> llen (x) == n 
        };

cons : (x : a) -> (xs : [a]) -> 
      State {\(h : heap). true} 
			v : { v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
				[h'=h] /\
            llen (v) == llen (xs) + 1 /\
            lmem (v, x) = true /\
            lhd (v) = x /\
            lsnd (v) = lhd (xs) /\
            last (v) = last (xs) /\
            pen (v) = pen (xs)

        };



hd : (l : [a]) -> 
      State {\(h : heap). true} 
			v : { v : a | true}
		{\(h : heap), (v : a), (h' : heap). 
				[h'=h] /\
            lmem (l, v) = true /\
            lhd (l) = v
            
        };


tl : (l : [a]) -> 
      State {\(h : heap). true} 
			v :{ v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
				[h'=h] /\
            llen (v) == llen (l) -- 1 /\
            last (v) = last (l) /\
            lhd (v) = lsnd (l) /\
            pen (v) = pen (l)

        };


nth : (l : [a]) -> (n : int) ->  
      State {\(h : heap). true} 
			v :{ v : a | true}
		{\(h : heap), (v : a), (h' : heap). 
			[h'=h] /\
            lmem (l, v) = true /\
            nth (l, n) = v 
        };



 append : (l1 : [a]) ->  (l2 : [a]) -> 
      State {\(h : heap). true} 
			v :{ v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
			[h'=h] /\
            llen (v) == llen (l1) + llen (l2) /\
            lhd (v) = lhd (l1) /\
            lsnd (v) = lsnd (l1) /\
            last (v) = last (l2) /\
            pen (v) = pen (l2)

        };


combine : (l1 : [a]) ->  (l2 : [a]) -> 
      State {\(h : heap). pllen (l1) == pllen (l2) 
            } 
			v :{ v : [apair] | true}
		{\(h : heap), (v : [apair]), (h' : heap). 
			   \(H : apair), (L : apair).
          [h'=h] /\
            pllen (v) == pllen (l1) /\
            plhd  (v) = H  /\
            pllast (v) = L /\
            ppr1 (H) = lhd (l1) /\
            ppr2 (H) = lhd (l2) /\
            ppr1 (L) = last (l1) /\
            ppr2 (L) = last (l2) 
            

        };


splitAt : (y:int) -> (l : [a]) -> {v : []} 


null : (l : [a]) -> {v : bool | [v=true] <=> llen (l) == 0};

elem : a -> [a] -> Bool

last : [a] -> a 

init : [a] -> [a]

take : int -> [a] -> [a]

drop : int -> [a] -> [a]


min : [a] -> a 

iterate :

repeat : 


replicate : 


cycle : 

takeWhile : 


dropWhile : 


break : 


span : 


strip :   


group : 

inits : 

goal : (l1:[a]) -> (l2 : [a]) -> 
 State {\(h : heap). pllen (l1) == pllen (l2)} 
			v :{ v : [apair] | true}
		{\(h : heap), (v : [apair]), (h' : heap). 
      \(H : apair), (L : apair).
			[h'=h] /\
            pllen (v) == pllen (l1)  /\
            (plhd  (v) = H  /\
            pllast (v) = L) => 
            (ppr1 (H) = lhd (l1) /\
            ppr2 (H) = last (l2) /\
            ppr1 (L) = last (l1) /\
            ppr2 (L) = lhd (l2))
            

        };

(*A simple example from Hoogle, 
 get the xth and yth elements and add it to the end of the list)
goal : (x:int) -> (y:int) -> (l:[a]) -> 
 State {\(h : heap). true} 
			v :{ v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
			[h'=h] /\
            llen (v) == llen (l) + 2/\
            lhd (v) =  lhd (l) /\
            lsnd (v) = lsnd (l) /\
            last (v) = nth (l, y) /\
            pen (v) = nth (l, x)  
        };

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

splitAt :: n:_ -> x:[a] -> ({v:[a] | (if (n >= 0) then (if (len x) < n then (len v) = (len x) else (len v) = n) else ((len v) = 0))},[a])<{\x1 x2 -> (len x2) = (len x) - (len x1)}>
span    :: (a -> GHC.Types.Bool) 
        -> xs:[a] 
        -> ({v:[a]|((len v)<=(len xs))}, {v:[a]|((len v)<=(len xs))})

break :: (a -> GHC.Types.Bool) -> xs:[a] -> ([a],[a])<{\x y -> (len xs) = (len x) + (len y)}>

reverse      :: xs:[a] -> {v: [a] | len(v) = len(xs)}

include <len.hquals>

GHC.List.!!         :: xs:[a] ->  (k : {v: _ | ((0 <= v) && (v < len(xs)))}) ->  {v:a| nth (xs,k) = v}


zip :: xs : [a] -> ys:[b]
            -> {v : [(a, b)] | ((((len v) <= (len xs)) && ((len v) <= (len ys)))
            && (((len xs) = (len ys)) => ((len v) = (len xs))) )}

zipWith :: (a -> b -> c) 
        -> xs : [a] -> ys:[b] 
        -> {v : [c] | (((len v) <= (len xs)) && ((len v) <= (len ys)))}

errorEmptyList :: {v: _ | false} -> a
