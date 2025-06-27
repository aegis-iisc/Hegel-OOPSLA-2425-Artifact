

(*remove the current user and nlmaining the invariant given in the query*)
goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = true /\ subscribe (v, n, u) = false}) -> 
                        (n  : { v : nl  | true}) -> 
		                (u : { v : user | true}) ->
                        {v : [nlrecord] |
                                nlmem (v, n, u) = true /\
                                subscribe (v, n, u) = true /\
                                Inv1 (*uniqueness*):= (\forall n1, n2: nl, u : user. ( [n1 != n2] /\ subscribe (v, n1, u) = true)  => subscribe (v, n2, u) = false)  /\
                                Inv2 (*minimal*) := (\forall n : nl. (n \in newsletters (v) => subsize (v, n) >= 1)
                                 }


(*A correct solution for the above query*)
\d, n, u.
    let nls = find_nls (d) (*these functions are defined as sql queries*) in 
    let subscriptions = List.filter (fun nl -> subscribed (nls, u)) nls in 
    if (List.size (subscriptions > 0)) then 
        (*unsubscribe the current newsletter*)
    else 
        let d2 = confirmS (d, n, u) in
        let d3 = review (d2, n, u) in 
        let (x1, d4) = promotions (d3, n, u) in 
        if (x1) then 
            let d' = add_email (d4) in 
            d'
        else 
            d4





