First, we update the \textit{Newsletter} schema with additional fields. The original {\it Newsletter} database in Cobalt (Figure 10 (a) in Cobalt~\cite{cobalt-tech}) has 4 fields {\it (\{ nl; user; code; articles\})}. 
We update the schema with additional fields creating a new \textit{Newsletter} schema, 
{\it (\{nl; user; promotions; email; code; subscribed; articles\})}.

Second, we must also update the libraries for the database, 
we add functions accessing these fields. For instance, for the current example, we add additional functions like {\sf udpate\_email}, {\sf is\_subscribed, notify, etc.,}. 
As a consequence of these changes, the underlying library usage protocol associated with the database also become more intricate. 


(* NLInsert *)
Given a newsletter and a user in the database, and subscribe the user to the newsletter, add the email for promotions 
nlInsert : (n  : { v : nl  | true}) -> 
	(u : { v : user | true}) -> 
	(d : {v: [nlrecord] | true}) -> 
	{v : ([nlrecord]) |  subscribed (v, n, u) = true 
	/\ promotions (snd (v), u) = true => (email (snd (v), u))}
	

(* NLRemove *)
nlRead : (n  : { v : nl  | true}) -> (u : { v : user | true}) -> 
(d : {v: [nlrecord] | true}) -> 

{v : ([nlrecord]) |  mem (fst (v), articles (snd (v))) = true 
/\ subscribed (snd (v), n, u) = false 
/\ promotions (snd (v), u) = true => (email (snd (v), u))}




(* NLReadRemove *)
nlReadRemove : (n  : { v : nl  | true}) -> (u : { v : user | true}) -> 
  (D : {v: [nlrecord] |  mem (v , n , u) = true}) -> 
  
  {v : ([string] * [nlrecord]) |  mem (fst (v), articles (snd (v))) = true 
  /\ subscribed (snd (v), n, u) = false /\ nlmem (snd (v), n, u) = false 
  /\ promotions (snd (v), u) = true => (email (snd (v), u) = true)}
  


Case1: The first set of queries are modified Cobalt queries 
which were challenging for cobalt when applied to larger database (and hence more complex protocol)
The new Newsletter data base now has the following schema : 
{n : nl; u : user; emailpromotions : bool; emailadd : string; confirmcode : bool; subscribed : bool}

(*Original Query for unsubscribing*)

goal : 	 (n  : { v : nl | true})-> 
		 (u : { v : user | true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						dsel (h, d) = D /\
						nlmem (D , n , u) = true /\
						subscribed (D, n, u) = true /\
						confirmed (D, n, u) = false}
				v : { v : unit | true}  
				{\(h: heap),(v : unit),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							(dsel (h', d) = D' /\ 
							dsel (h, d) = D) => 
							(nlmem (D', n, u) = true /\
							subscribed (D', n, u) = false)
				};

(* Functionalize the query *)
goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = false}) -> 
(n  : { v : nl | true}) -> 
(u : { v : user | true}) -> {v : [nlrecord] | nlmem (v, n, u) = true /\ subscribed (v, n, u) = false };



(*
Rather than unsubscribing this directly, 
we first need to add 
user and newsletter to the table, 
add a review for the newsletter
then confirm the unsubscribing and finally unsubsribe*)
\ D, n, u -> 
        unsubsribe if (emailpromotions (review ((confirmU D n u) n u))
                 then unsubscribe (remove_email)
                    else 
                        unsubscribe
goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = false}) -> 
                        (n  : { v : nl | true}) -> 
		                (u : { v : user | true}) ->
                        {v : [nlrecord] | nlmem (v, n, u) = true /\
							subscribed (v, n, u) = false }




(*Original query for subscribing, file small_query2*)


goal : 	 (n  : { v : nl | true})-> 
		 (u : { v : user | true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						dsel (h, d) = D /\
						nlmem (D , n , u) = true /\
						subscribed (D, n, u) = false /\
						confirmed (D, n, u) = false}
				v : { v : unit | true}  
				{\(h: heap),(v : unit),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							(dsel (h', d) = D' /\ 
							dsel (h, d) = D) => 
							(nlmem (D', n, u) = true /\
							subscribed (D', n, u) = true /\
							confirmed (D', n, u) = false)
				};

(*
Added more fields to the database, this will allow us to define bigger protocols which are harder to 
synthesize.
\ D, n, u -> 
        subsribe if (agreeemails ((confirmS 
                                (insert D n u) 
                                n u))) then 
                 subscribe (add_email (_))
                 else 
                    subscribe
                 n u))
*)
goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = false}) -> 
                        (n  : { v : nl  | true}) -> 
		                (u : { v : user | true}) ->
                        {v : [nlrecord] | nlmem (v, n, u) = true /\
							subscribed (v, n, u) = true }



(*Original query to remove Newsletter*)
	 
goal : 	 (n  : { v : nl | true})-> 
		 (u : { v : user | true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						dsel (h, d) = D /\
						nlmem (D , n , u) = true /\
						subscribed (D, n, u) = true /\
						confirmed (D, n, u) = false}
				v : { v : unit | true}  
				{\(h: heap),(v : unit),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							(dsel (h', d) = D' /\ 
							dsel (h, d) = D)
							=> (nlmem (D', n, u) = false) 
				};
	

(*\ D, n, u -> 
    email_promotions. review . confirmU        
    if (email_promotions = false) then remove . unsubscribe. remove_email
    else 
        remove_email . unsubscribe 
*)         

goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = false}) -> 
                        (n  : { v : nl  | true}) -> 
		                (u : { v : user | true}) ->
                            ??


(*Original Query for readRemove*)	 
goal : 	 (n  : { v : nl | true})-> 
		 (u : { v : user | true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						dsel (h, d) = D /\
						nlmem (D , n , u) = true /\
						subscribed (D, n, u) = true /\
						confirmed (D, n, u) = false }
				v : { v : [string] | true}  
				{\(h: heap),(v : [string]),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							(dsel (h', d) = D' /\ 
							dsel (h, d) = D ) => 
								(v = articles (D') /\
								nlmem (D', n, u) = false)};
	
goal : (D : {v: [nlrecord] |  nlmem (v , n , u) = true}) -> 
                        (n  : { v : nl  | true}) -> 
		                (u : { v : user | true}) ->
                        {v : ([string] * [nlrecord]) |
                                fst (v) = articles (snd (v)) /\
                                nlmem (snd (v), n, u) = false
                                 }


(*Similarly other benchmarks are to be extended*)


Case 2: Extend the benchmarks with complex queries which will require richer libraries and invaraints.
e.g. Extended Newsletter example, 
with a database invaraint that each user is subscribed to a uniue newsletter and each newsletter is subscribed by atleas 1 newsletter.
This requires other library functions like find\_subscribed, if\_subscribed, etc. 
Consider the query to subscribe a user to a newsletter.

(*remove the current user and nl	 

*)
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
&$\lambda$& d, n, u.
    let nls = find_nls (d) (*these functions are defined as sql queries*) in 
    let subscriptions = List.filter (fun nl -> subscribed (nls, u)) nls in 
    if (List.size (subscriptions > 0)) then 
        (*unsubscribe the current newsletter*)
    else 
        let d2 = confirmS (d, n, u) in
        let d3 = review (d2, n, u) in 
        let (x1, d4) = promotions (D3, n, u) in 
        if (x1) then 
            let d' = add_email (d4) in 
            d'
        else 
            d4


(* FWInsert *)
(* Original query *)

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
	
(* FWMKCentral *)

(* Original  *)
goal : (d : { v : int | true}) -> 
	(x : { v : int | not [v=d]}) -> 		
				State {\(h: heap).
						 \(D : [int]),(CS : [srpair]).
						 didsel (h, dtab) = D /\ 
						 device (D, d) = true /\
						 dcssel (h, cstab) = CS /\
														 device (D, x) = true /\
														 central (CS, d) = true /\
														 central (CS, x) = false} 
						 v : {v : unit | true} 
							{\(h: heap),(v : unit),(h': heap).
								\(D: [int]),(D' : [int]),(CS' : [srpair]).
																 (dcssel (h', cstab) = CS' /\   
								didsel (h', dtab) = D') =>	
							 (device (D', d) = false /\ 
																 device (D', x) = true /\ 
																 central (CS', d) = false /\
																 central (CS', x) = true)
							};
(* Change the database  to increase the size*)
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