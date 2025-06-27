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



copy : (a1 : ref vec) -> 
            State {\(h : heap).
                \(V1: vec). 
                        vdom (h, a1) = true 
                 } 
			     v : { v : ref vec | true} 
                {\(h : heap), (v : ref vec), (h' : heap). 
				 \(V1: vec), (VN : vec). 
                    vdom (h', a1) = true /\
                    vdom (h' , v) = true /\
                    vsel (h, a1) = V1 /\ 
                    vsel (h, v) = VN /\
                    vsel (h', a1) = vsel (h, a1) /\
                    vlen (VN) == vlen (V1)
                    
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
