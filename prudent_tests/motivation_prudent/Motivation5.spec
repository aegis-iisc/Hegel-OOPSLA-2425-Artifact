
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
(*zip two list by reversing the second list*)
(*one concern is, is coming up with the program is equivalent to the 
coming up with the spec
- x:[a] -> y:[b] -> [(a, b)]

[1,2]
[3,4]
[(1,3), (2,4)]

['a','b']
['c','d']
[('a','c'),('b','d')]

Finds a solution: \x y. zip x y 

But if we refine the query to first reverse the second list (or the first list) then times out.

[1,2]
[3,4]
[(1,4), (2,3)]

['a','b']
['c','d']
[('a','d'),('b','c')]

No solution: Required output: \x y. zip x (reverse y)




*)
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

        

