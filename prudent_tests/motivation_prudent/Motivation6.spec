
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

elem : Eq a => a -> [a] -> Bool

last : [a] -> a 

init 

take n list 

(*
given two indecies, split the list into two based on the second and take take the 

x:Int -> y:Int -> z:[a] -> ([a], [a])

-- Refine it to deconstruct the pair and take x element from the first projection

1
2
[49, 62, 82, 54, 76]
([49],[82,54,76])

2
3
[49, 62, 82, 54, 76]
([49,62],[54,76])


- Required Solution: ((take x (fst (splitAt y+1 z))), snd (splitAt (y+1) z))
- simpler solution:   take x (z) , rev (drop y (z))
More complicated query
    take x (rev (fst split y z), rev (snd (split y z)))



2
3
[49, 62, 82, 54, 76]
([82, 62],[76,54])





*)
goal : (x:int) -> (y : int) -> (z : {v : [a] | llen (v) >= x /\ llen (v) >= y})
     	-> { v : plist |  \(H : [a]), (L : [a]).
		    (fst (v) = H  /\
            snd (v) = L ) => 
            llen (H) = x /\
            llen (L) = y /\
            \(u : a). lmem (H, u) = true => lmem (z, u) /\
            \(u : a). lmem (L, u) = true => lmem (z, u) /\
            lord (H) C= lord (z) /\
            lord (L) C= lord (z) 

        };

        
backward-goal {v : [a] | llen (v) == llen (z) - y /\ ord, mem properties}        

size0

x  (incorrect base type)         


y  (incorrect base type)



z : [a] (correct base type) 
