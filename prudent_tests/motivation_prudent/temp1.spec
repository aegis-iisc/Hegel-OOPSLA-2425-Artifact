type vec;

qualifier vdom : heap :-> ref vec :-> bool;
qualifier vmem : vec :-> a :-> bool;
qualifier vsel : heap :-> ref vec :-> vec;
qualifier vlen : vec :-> int;
qualifier vdisjoint : vec :-> vec :-> bool;

Max : int;
num : ref int;
V2 : vec;
V2' : vec;





type ziplist;
qualifier zdom : heap :-> ref ziplist :-> bool; 
qualifier zsel : heap :-> ref ziplist :-> ziplist;
qualifier zlen : ziplist :-> int; 
qualifier zllen : ziplist :-> int; 
qualifier zrlen : ziplist :-> int;
qualifier zmem : ziplist :-> a :-> bool;
qualifier allen : [a] :-> int;

Z : ziplist;
Z' : ziplist;





set : (vec : ref vec) -> 
      (n : int) ->  
      (x: a) -> 
           State {\(h : heap).
                        \(V: vec). 
                        vdom (h, vec) = true 
                } 
			    v : { v : unit | true}   
                {\(h : heap), (v : unit), (h' : heap). 
				    \(V : vec), (V' : vec).
	                vsel (h, vec) = V /\
                    vsel (h', vec) = V' /\
                    vmem (V', x) = true /\
                    (vlen (V') > n \/ vlen (V') == n) 
                    
                };


is_empty : (vec : ref vec) ->  
                State {\(h : heap). vdom (h, vec) = true} 
			    v : { v : bool | true}   
                {\(h : heap), (v : bool), (h' : heap). 
				    \(V : vec), (V' : vec).
	                  vsel (h, vec) = V /\
                      ([v = true] <=> len (V) = 0) /\ 
                      [h' = h]
                    };




copy : (a1 : ref vec) -> 
            State {\(h : heap).
                \(V1: vec). 
                        vdom (h, a1) = true 
                 } 
			     v : { v : ref vec | true} 
                {\(h : heap), (v : ref vec), (h' : heap). 
				 \(V1: vec), (VN : vec), (V1' : vec). 
                    vdom (h', a1) = true /\
                    vdom (h' , v) = true /\
                    vsel (h, a1) = V1 /\ 
                    vsel (h, v) = VN /\
                    vsel (h', a1) = vsel (h, a1) /\
                    [VN = V1] /\
                    not [a1 = v] /\
                    Max > (vlen (V1) + vlen (VN)) 
                };


get : (vec : ref vec) -> 
        (n : int) ->  
           State {\(h : heap).
                        \(V: vec). 
                        vdom (h, vec) = true /\ 
                        (vsel (h, vec) = V => vlen (V) > n)
                } 
			    v : { v : a | true}   
                {\(h : heap), (v : a), (h' : heap). 
				    \(V : vec).
	                vsel (h, vec) = V /\
                        vmem (V, v) = true /\        
                         [h' = h]
                };


create : (capacity : { v : int | ( [v > 0] \/ [v=0]) /\ not [Max > v]}) -> 
         (dummy : a) -> 
       	 State {\(h : heap). not (sel (h, num) > 1)} 
			v : ref vec 
		 {\(h : heap), (v : ref vec), (h' : heap). 
				\(V : vec), (V' : vec).
			      vdom (h, v) = false /\
                  sel (h', num) == sel (h, num) + 1 /\
                  vdom (h', v) = true /\
                  vsel (h', v) = V' /\
                  vlen (V') == 0
        };


      
length :  (vec : ref vec) ->  
                State {\(h : heap). vdom (h, vec) = true} 
			    v : { v : int | true}   
                {\(h : heap), (v : int), (h' : heap). 
		        \(V : vec).
	                v = vlen (V) /\
                      [h' = h]
                    };
       


clear : (vec : ref vec) ->  
            State {\(h : heap). vdom (h, vec) = true} 
			 v : { v : unit | true}    
             {\(h : heap), (v : unit), (h' : heap). 
		\(V : vec), (V' : vec).
	            vsel (h', vec) = V' /\ 
                vlen (V') == 0 /\
                vdom (h', vec) = true 
            };



lengthzl : (z : ref ziplist)  ->
                        State {\(h : heap). true} 
		            	    v : {v : int | true} 
		                { \(h : heap), (v : int), (h' : heap). 
				        \(Z : ziplist).
		                    zsel (h, z) = Z /\
                            zlen (Z) = v /\
                            [h=h'] 
                        };
          


to_list : (z : ref ziplist)  ->
                        State {\(h : heap). true} 
		            	    v : [a] 
		                { \(h : heap), (v : [a]), (h' : heap). 
				        \(Z : ziplist).
		                    zsel (h, z) = Z /\
                            allen (v) == zlen (Z) /\
                            [h=h']
                        };
         


goal :  (n : int) -> 
        (m : int) -> 
        (a1 : ref vec) -> 
       State {\(h : heap).
                  \(V1: vec).
                  vdom (h, a1) = true /\ 
                  vsel (h, a1) = V1 /\
                  sel (h, num) == 1 /\
                  vlen (V1) > n 
             } 
			     v : { v : ref vec | true} 
                {\(h : heap), (v : ref vec), (h' : heap). 
		        \(V1: vec), (V1' : vec). 
                    vsel (h, a1) = V1 /\ 
                    vsel (h', a1) = V1' /\
                    (vlen (V1') > m \/ vlen (V1') == m) 
                    
                };
