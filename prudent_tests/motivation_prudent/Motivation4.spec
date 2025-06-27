

qualifier llen : [a] :-> int;
qualifier lmem : [a] :-> a :-> bool;
qualifier lhd : [a] :-> a;
qualifier last  : [a] :-> a;
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


is_empty : (l : [a]) ->  
                State {\(h : heap). true} 
			    v : { v : bool | true}   
                {\(h : heap), (v : bool), (h' : heap). 
				      [h' = h] /\
                      ([v = true] <=> 
                      (llen (l) = 0) /\ 
                      lhd (l) = ep /\
                      last (l) = ep /\
                      lsnd (l) = ep /\
                      pen (l) = ep)
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



(*reverse the list and add to the tail of the original list*)
goal : (l:[a]) -> 
 State {\(h : heap). true} 
			v :{ v : [a] | true}
		{\(h : heap), (v : [a]), (h' : heap). 
			[h'=h] /\
            llen (v) == llen (l) + llen (l) /\
            lhd (v) =  lhd (l) /\
            lsnd (v) = lsnd (l) /\
            last (v) = lhd (l) /\
            pen (v) = lsnd (l)  
        };

