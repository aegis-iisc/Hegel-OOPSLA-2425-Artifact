nlInsert : (n  : { v : nl  | true}) -> 
	(u : { v : user | true}) -> 
	(d : {v: [nlrecord] | true}) -> 
	{v : ([nlrecord]) |  subscribed (v, n, u) = true 
	/\ promotions (snd (v), u) = true => (email (snd (v), u))}
	

(* Solution *)
\n, u, d.
if (is_subscribed (d, n, u)) then   
  let x1 = promotions (d, n, u) in 
   if (x1) then 
       let d = add_email (d, u) in
       return d 
    else
       return d     
else
  let d1 = confirmS (d, n, u) in 
  let d2 = subscribe (d1, n, u) in 
  let x1 = promotions (d, n, u) in      
  if (x1) then 
    let d = add_email (d, u) in
    return d 
 else
    return d  
    





