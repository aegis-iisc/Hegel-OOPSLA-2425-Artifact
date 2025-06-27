
(* FWMKCentral *)

(* Change the database  to increase the size *)
goal: 
  (sr : [srpair]) -> 
	(dtable : [int]) -> 			
	(d : { v : int | true}) -> 
	(x : { v : int | true }) -> 	

	{v : ([srpair]*[int]) | 
		device (snd (v), d) = false /\
		device (snd (v), x) = true  /\
		central (fst (v), d) = false /\
		central (fst (v), x) = true 
  }	

\sr, dtable, d, x.														
  if (x=d) then	
  	bottom
  else 
  	if (is_central (srpair,d)) then
  		let dtable = add_device (dtable, x) in 
  		let sr = remove_central (sr, d) in 
  		let sr = mk_central (sr, x)
  		let sr = add_pair (sr, d, x) in 
  		return (sr, dtable)
    else 
  		let dtable = add_device (dtable, x) in 
  		let sr = mk_central (sr, x)
  		let sr = add_pair (sr, d, x) in 
  		return (sr, dtable)