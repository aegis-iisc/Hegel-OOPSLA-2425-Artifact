
We update the schema with additional fields creating a new \textit{Newsletter} schema, 
{\it (\{nl; user; promotions; email; code; subscribed; articles\})}.


(* Read an article for the given user and newsletter *)
nlReadRemove : (n  : { v : nl  | true}) -> (u : { v : user | true}) -> 
  (D : {v: [nlrecord] |  mem (v , n , u) = true}) -> 
  
  {v : ([string] * [nlrecord]) |  mem (fst (v), articles (snd (v))) = true 
  /\ subscribed (snd (v), n, u) = false /\ nlmem (snd (v), n, u) = false 
  /\ promotions (snd (v), u) = true => (email (snd (v), u) = true)}
  



(* Expedted Solution *)

\n, u, d.
  
       let article = read (n, u) in 
       let x1 = promotions (d, n, u) in 
        if (x1) then 
            let d = add_email (d, u) in 
            let d = confirmU (d, n, u) in 
            let d = unsubscribe (d, n, u) in 
            let d = remove (d, n, u) in 
            
            return (article, d)
        else 
          let d = confirmU (d, n, u) in 
          let d = unsubscribe (d, n, u) in 
          let d = remove (d, n, u) in 
          return (article, d)
    