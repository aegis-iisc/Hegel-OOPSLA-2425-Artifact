
(* FWInsert *)
(* Original query in Cobalt *)

goal : (d : { v : int | true}) -> 
	(x : { v : int | not [v = d]}) -> 		
				State {\(h: heap).
						 \(D : [int]), (CS : [srpair]).
						 didsel (h, dtab) = D /\	
						 dcssel (h, cstab) = CS /\
														 device (D, d) = true    
						 } 
						 v : {v : unit | true} 
							{\(h: heap),(v : unit),(h': heap).
								\(D' : [int]),(CS' : [srpair]). 
								(didsel (h', dtab) = D' /\
							 dcssel (h', cstab) = CS' ) =>  
							 
							 ( 
							 device (D', x) = true /\ 
							 cansend (CS', d, x) = true) 
							};

(* Functionalize *)
goal :
	(sr : [srpair]) -> 
	(dtable : [int]) -> 		
	(d : { v : int | true}) -> 
	(x : { v : int | true}) -> 		
		{v : ([srpair] * [int]) | device (snd (v), x) = true /\ cansend (fst (v), d, x) = true
														/\ 	(\forall d1 d2. is_central (d1) => not is_central d2)}


(*Solution  *)
\sr, dtable, d, x.														
if (x=d) then	
	let sr = add_pair (sr, x, x) in 
	return (sr, dtable)
else 
	let dtable = add_device (dtable, d) in 
	let sr = add_pair (sr, d, x) in 
	return (sr, dtable)