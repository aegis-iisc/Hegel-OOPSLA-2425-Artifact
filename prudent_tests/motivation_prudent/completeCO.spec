D : [nlrecord];
D' : [nlrecord];
d : ref [nlrecord];


(*TODO Convert these into functional versions*)
select : (n  : { v : nl | true})
							-> (u : { v :user | true}) -> 
									 
									 State {\(h : heap).
									 	\(D : [nlrecord]).
									 	true} 
				D : [nlrecord];
D' : [nlrecord];
d : ref [nlrecord];



select : (n  : { v : nl | true})
							-> (u : { v :user | true}) -> 
									 
									 State {\(h : heap).
									 	\(D : [nlrecord]).
									 	true} 
										v : { v : unit | true}
									   {\(h: heap),(v : unit),(h': heap).
										\(D : [nlrecord]), (D' : [nlrecord]).
										dsel (h', d) = D' /\
										dsel (h, d) = D /\
										D' = D /\
										nlmem (D, n, u) = true
										};


confirmS :  (n  : { v : nl | true})-> 
		  (u : { v : user | true}) -> 
		State {\(h:heap).
				\(D : [nlrecord]).
				(dsel (h, d) = D =>  (subscribed (D, n, u) = false /\ confirmed (D, n, u) = false))}
			v : {v : unit | true}
			{ \(h: heap),(v : unit),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				subscribed (D', n, u) = false /\ 		
				nlmem (D', n, u) = true /\
				confirmed (D', n, u) = true};






subscribe : (n  : { v : nl | true})-> 
			 (u : { v : user | true}) -> 
					State {\(h : heap). 
							\(D : [nlrecord]).
								dsel (h, d) = D => 
									(nlmem (D , n , u) = true /\ confirmed (D, n, u) = true
									/\ subscribed (D, n, u) = false)}
					v : { v : unit | true}  
						{\(h: heap),(v : unit),(h': heap).
							\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D'/\
							dsel (h, d) = D /\
							nlmem (D', n, u) = true /\
							subscribed (D', n, u) = true /\
							confirmed (D', n, u) = false		
							};	




read :  (n  : { v : nl | true})-> 
		(u : { v : user | true}) -> 
		State {\(h : heap). 
				\(D : [nlrecord]).
					dsel (h, d) = D =>
						(nlmem (D , n , u) = true /\ 
						subscribed (D, n, u) = true /\
						confirmed (D, n, u) = false 
						)
				}
				v : { v : [string] | true}  
			{\(h: heap),(v : [string]),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				nlmem (D', n, u) = true /\
				subscribed (D', n, u) = true /\ 		
				confirmed (D', n, u) = false /\
				v = articles (D')};





		
		 
remove : (n  : { v : nl | true})-> 
		 (u : { v : user| true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						(dsel (h, d) = D =>
							(nlmem (D , n , u) = true /\
							subscribed (D, n, u) = false) 
						)	
					}
				v : { v : unit | true}  
				{\(h: heap),(v : unit),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D' /\ 
							dsel (h, d) = D /\
							nlmem (D', n, u) = false 
				};
		 



unsubscribe : (n  : { v : nl | true})-> 
			 (u : { v : user | true}) -> 
					State {\(h : heap). 
							\(D : [nlrecord]).
								dsel (h, d) = D => 
									(nlmem (D , n , u) = true /\ confirmed (D, n, u) = true /\
									subscribed (D, n, u) = true)}
					v : { v : unit | true}  
						{\(h: heap),(v : unit),(h': heap).
							\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D'/\
							dsel (h, d) = D /\
							nlmem (D', n, u) = true /\
							subscribed (D', n, u) = false /\
							confirmed (D', n, u) = false		
									
							};	




confirmU :  (n  : { v : nl | true}) -> 
		    (u : { v : user | true}) -> 
		State {\(h:heap).
				\(D : [nlrecord]).
				(dsel (h, d) = D =>  (subscribed (D, n, u) = true /\ confirmed (D, n, u) = false))}
			v : {v : unit | true}
			{ \(h: heap),(v : unit),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				subscribed (D', n, u) = true /\ 		
				nlmem (D', n, u) = true /\
				confirmed (D', n, u) = true};



		 
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
		 

						v : { v : unit | true}
									   {\(h: heap),(v : unit),(h': heap).
										\(D : [nlrecord]), (D' : [nlrecord]).
										dsel (h', d) = D' /\
										dsel (h, d) = D /\
										D' = D /\
										nlmem (D, n, u) = true
										};


confirmS :  (n  : { v : nl | true})-> 
		  (u : { v : user | true}) -> 
		State {\(h:heap).
				\(D : [nlrecord]).
				(dsel (h, d) = D =>  (subscribed (D, n, u) = false /\ confirmed (D, n, u) = false))}
			v : {v : unit | true}
			{ \(h: heap),(v : unit),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				subscribed (D', n, u) = false /\ 		
				nlmem (D', n, u) = true /\
				confirmed (D', n, u) = true};






subscribe : (n  : { v : nl | true})-> 
			 (u : { v : user | true}) -> 
					State {\(h : heap). 
							\(D : [nlrecord]).
								dsel (h, d) = D => 
									(nlmem (D , n , u) = true /\ confirmed (D, n, u) = true
									/\ subscribed (D, n, u) = false)}
					v : { v : unit | true}  
						{\(h: heap),(v : unit),(h': heap).
							\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D'/\
							dsel (h, d) = D /\
							nlmem (D', n, u) = true /\
							subscribed (D', n, u) = true /\
							confirmed (D', n, u) = false		
							};	




read :  (n  : { v : nl | true})-> 
		(u : { v : user | true}) -> 
		State {\(h : heap). 
				\(D : [nlrecord]).
					dsel (h, d) = D =>
						(nlmem (D , n , u) = true /\ 
						subscribed (D, n, u) = true /\
						confirmed (D, n, u) = false 
						)
				}
				v : { v : [string] | true}  
			{\(h: heap),(v : [string]),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				nlmem (D', n, u) = true /\
				subscribed (D', n, u) = true /\ 		
				confirmed (D', n, u) = false /\
				v = articles (D')};





		
		 
remove : (n  : { v : nl | true})-> 
		 (u : { v : user| true}) -> 
				State {\(h : heap). 
						\(D : [nlrecord]).
						(dsel (h, d) = D =>
							(nlmem (D , n , u) = true /\
							subscribed (D, n, u) = false) 
						)	
					}
				v : { v : unit | true}  
				{\(h: heap),(v : unit),(h': heap).
						\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D' /\ 
							dsel (h, d) = D /\
							nlmem (D', n, u) = false 
				};
		 



unsubscribe : (n  : { v : nl | true})-> 
			 (u : { v : user | true}) -> 
					State {\(h : heap). 
							\(D : [nlrecord]).
								dsel (h, d) = D => 
									(nlmem (D , n , u) = true /\ confirmed (D, n, u) = true /\
									subscribed (D, n, u) = true)}
					v : { v : unit | true}  
						{\(h: heap),(v : unit),(h': heap).
							\(D : [nlrecord]), (D' : [nlrecord]).
							dsel (h', d) = D'/\
							dsel (h, d) = D /\
							nlmem (D', n, u) = true /\
							subscribed (D', n, u) = false /\
							confirmed (D', n, u) = false		
									
							};	




confirmU :  (n  : { v : nl | true}) -> 
		    (u : { v : user | true}) -> 
		State {\(h:heap).
				\(D : [nlrecord]).
				(dsel (h, d) = D =>  (subscribed (D, n, u) = true /\ confirmed (D, n, u) = false))}
			v : {v : unit | true}
			{ \(h: heap),(v : unit),(h': heap).
				\(D : [nlrecord]), (D' : [nlrecord]).
				dsel (h', d) = D'/\
				dsel (h, d) = D /\
				subscribed (D', n, u) = true /\ 		
				nlmem (D', n, u) = true /\
				confirmed (D', n, u) = true};



		 
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
		 



dtab : ref [int];
cstab : ref [srpair];
D : [int];
CS : [srpair];
D' : [int];
CS' : [srpair];


add_device : (d : { v : int | true}) -> State {
										\(h : heap).	
										\(D : [int]), (CS : [srpair]).
										didsel (h, dtab) = D =>		
										device (D, d) = false}
										v : {v : unit | true}
										{\(h: heap),(v : unit),(h': heap).
											\(D : [int]), (D' : [int]).
											didsel (h, dtab) = D /\		
											didsel (h', dtab) = D' /\
											dcssel (h', cstab) = dcssel (h, cstab) /\
											device (D', d) = true	/\
											dsize (D') == dsize (D) + 1 	
										};  




make_central : (d : { v : int | true}) -> State {
										\(h : heap).
											\(D : [int]), (CS : [srpair]).
											(didsel (h, dtab) = D /\ dcssel (h, cstab) = CS) =>	
											(device (D, d) = true /\ central (CS, d) = false)											}
											v :  { v : unit | true}
										 { \(h: heap),(v : unit),(h': heap).
												\(CS : [srpair]), (CS' : [srpair]).
										 		didsel (h', dtab) = didsel (h, dtab) /\
												dcssel (h', cstab) = CS' /\
												central (CS', d) = true
										 };




diff_device : (d : { v : int | true}) -> State {
										\(h : heap).
											\(D : [int]), (CS : [srpair]).
											didsel (h, dtab) = D =>	
											dsize (D) > 1}
											v : {v : int | true}
											{\(h: heap),(v : int),(h': heap).
												\(D : [int]), (D' : [int]),(CS : [srpair]),(CS' : [srpair]).
												didsel (h', dtab) = didsel (h, dtab) /\
												dcssel (h', cstab) =  dcssel (h, cstab) /\
												device (D', v) = true /\ 
												not ([v = d])
											}; 


add_connection : (s : { v : int | true}) 
					-> (r : { v : int | true}) -> 
									State {
										\(h : heap).
											\(D : [int]).
											didsel (h, dtab) = D =>	
											(device (D, s) = true /\ 
											device (D, r) = true)	
											}
											v : {v : unit | true}
											{\(h: heap),(v : unit),(h': heap).
												\(D : [int]), (D' : [int]),(CS : [srpair]),(CS' : [srpair]).
												didsel (h', dtab) = didsel (h, dtab) /\
												dcssel (h', cstab) = CS' /\
												cansend (CS', s, r) = true 
											}; 

delete_device : (d : { v : int | true}) -> 
				(y : { v : int | not [v = d]}) -> 
								State {\(h : heap).
											\(D : [int]),(CS : [srpair]).
											(didsel (h, dtab) = D /\
											dcssel (h, cstab) = CS )=>	
											(
												device (D, d) = true /\ 
												device (D, y) = true /\ 
												central (CS, y) = true 
                                          		)}
									v : {v : unit | true}
								 { \(h: heap),(v : unit),(h': heap).
										\(D : [int]), (D' : [int]),(CS' : [srpair]).
										 didsel (h', dtab) = D' /\
										 dcssel (h', cstab) = CS' /\
										 device (D', d) = false /\
                                         device (D', y) = true /\
                                         
										 central (CS', y) = true 
								 };		 


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


(*Add the vocal library*)

(*HashTable*)
type key;
type table;
qualifier hdom : heap :-> ref table :-> bool;
qualifier hsel : heap :-> ref table :-> table;
qualifier hmem : table :-> key :-> bool;
qualifier hsize : table :-> int;  
qualifier hvmem : table :-> a :-> bool;
qualifier hlen : [a] :-> int;
qualifier keyset : table :-> [key];

create : (n : int) -> 
         State {\(h : heap). true} 
			v : ref table 
		{ \(h : heap), (v : ref table), (h' : heap). 
				\(H' : table).
			      hdom (h', v) = true /\
                  hsel (h', v) = H' /\
                  hsize (H') = 0};


clear : (ht : ref table) -> 
         State {\(h : heap). hdom (h, ht) = true} 
			v : {v : unit | true} 
		{ \(h : heap), (v : unit), (h' : heap). 
				\(H' : table), (H : table).
			      hdom (h', ht) = true /\
                  hsel (h', ht) = H' /\
                  hsize (H') = 0};



reset : (ht : ref table) -> 
         State {\(h : heap). hdom (h, ht) = true} 
			v : {v : unit | true} 
		{ \(h : heap), (v : unit), (h' : heap). 
				\(H' : table), (H : table).
			      hdom (h', ht) = true /\
                  hsel (h', ht) = H' /\
                  hsize (H') = 0};





add :  (ht : ref table)  -> 
       (k : key) ->
       (val : a) -> 
       State {\(h : heap).
                        \(H : table).     
                        hdom (h, ht) = true /\
                        (hsel (h, ht) = H => hmem (H, k) = false)} 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
				 \(H : table), (H' : table). 
                    hsel (h, ht) = H /\ 
                    hsel (h', ht) = H' /\
                    hmem (H', k) = true /\
                    hvmem (H', val) = true /\
                    hsize (H') ==  hsize (H) + 1
                };




copy : (ht1 : ref table) -> 
            State {\(h : heap).
                \(H1: table). 
                        hdom (h, ht1) = true
                 } 
			     v : { v : ref table | true} 
                {\(h : heap), (v : ref table), (h' : heap). 
				 \(H1: table), (HN : table). 
                    hdom (h', v) = true /\
                    hsel (h, ht1) = H1 /\ 
                    hsel (h', v) = HN /\
                    hsel (h', ht1) = hsel (h, ht1) /\
                    hsize (HN) = hsize  (H1) 
                };



population: (ht1 : ref table) -> 
            State {\(h : heap).
                \(H1: table). 
                        hdom (h, ht1) = true
                 } 
			     v : { v : int | true} 
                {\(h : heap), (v : int ), (h' : heap). 
				 \(H1: table). 
                    hsel (h, ht1) = H1 /\ 
                    hsel (h', ht1) = hsel (h, ht1) /\
                    v = hsize (H1)
                };

length : (ht1 : ref table) -> 
            State {\(h : heap).
                \(H1: table). 
                        hdom (h, ht1) = true
                 } 
			     v : { v : int | true} 
                {\(h : heap), (v : int ), (h' : heap). 
				 \(H1: table). 
                    hsel (h, ht1) = H1 /\ 
                    hsel (h', ht1) = hsel (h, ht1) /\
                    v = hsize (H1)
                };


iter: (k : key) -> 
     (f : (val : a) -> unit) -> 
     (ht : ref table) -> 
     unit;

fold: (f : (k : key) -> (v : a) -> (i: b) -> b) -> 
        (ht : ref table) -> 
        (init : b) -> 
        {res : b | true};


remove :  (ht : ref table)  -> 
       (k : key) ->
       State {\(h : heap).
                           \(H : table).
                  hdom (h, ht) = true /\
                  (hsel (h, ht) = H => hmem (H,k) = true)
                } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
				 \(H: table), (H' : table). 
                    hdom (h', ht) = true /\
                    hsel (h, ht) = H /\ 
                    hsel (h', ht) = H' /\
                    hmem (H', k) = false /\
                    hsize (H') ==  hsize (H) -- 1
                };

 mem: (ht : ref table)  -> 
       (k : key) ->
       State {\(h : heap).
                  hdom (h, ht) = true 
                 } 
			     v : { v : bool | true} 
                {\(h : heap), (v : bool), (h' : heap). 
				 \(H: table), (H' : table). 
                    hsel (h, ht) = H /\ 
                    hsel (h', ht) = H' /\
                    [H' = H] /\
                    ([v = true] <=> (hmem (H, k) = true)) /\
                     ([v = false]<=> (hmem (H, k) = false)) 
                    
                };


goal1 : (ht : ref table)  -> 
       (k : key) ->
       (val : a) ->  
        State {\(h : heap).
                    \(H : table).
                  hdom (h, ht) = true /\
                  hsel (h, ht) = H /\
                  hmem (H,k) = true
                 } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
				 \(H: table), (H' : table). 
                    (hsel (h, ht) = H /\ 
                    hsel (h', ht) = H') => 
                    (hvmem (H', val) = true /\
                     hmem (H', k) = true /\
                     hsize (H') = hsize (H))
                 
                };

goal2 : 
(ht : ref table)  -> 
       (k : key) ->
       (val : a) ->  
        State {\(h : heap).
                  hdom (h, ht) = true 
                  } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
				 \(H: table), (H' : table). 
                    (hsel (h, ht) = H /\ 
                    hsel (h', ht) = H') => 
                    (hvmem (H', val) = true /\
                    hmem (H', k) = true)
                 
                };





goal3 : (ht : ref table)  -> 
       (k : key) ->
       (val : a) ->  
        State {\(h : heap).
                \(H : table).
                  hdom (h, ht) = true /\
                  hsel (h, ht) = H /\
                  hmem (H, k) = false
                 } 
			     v : { v : ref table | true} 
                {\(h : heap), (v : ref table), (h' : heap). 
				 \(H: table), (HN : table). 
                    (hsel (h, ht) = H /\ 
                    hsel (h', ht) = HN) => 
                    ( hvmem (HN, val) = true /\
                    hmem (HN, k) = true /\
                    hsize (HN) = hsize  (H) 
                     )
                 
                };


(*Priority Queue*)
type pq;
qualifier pqdom : heap :-> ref pq :-> bool;
qualifier pqsel : heap :-> ref pq :-> pq;
qualifier pqlen : pq   :-> int; 
qualifier pqmem : pq   :-> int :-> bool;
qualifier minimum : pq :-> int  :-> bool;

Top : int;

create : State {\(h : heap). true} 
			v : ref pq 
		{\(h : heap), (v : ref pq), (h' : heap). 
				\(P : pq), (P' : pq).
			            pqdom (h', v) = true  /\
                  pqsel (h', v) = P' /\
                  pqlen (P') = 0 /\
                  minimum (P') = Top
    };


is_empty : (pqueue: ref pq) ->  
                State {\(h : heap). pqdom (h, pqueue) = true} 
			    v : { v : bool | true}   
            {\(h : heap), (v : bool), (h' : heap). 
				      \(P : pq).
	                pqsel (h, pqueue) = P /\
                  ([v = true] <=> pqlen (P) = 0) /\ 
                  [h' = h]
            };


size :  (pqueue : ref pq) ->  
                State {\(h : heap). 
                    pqdom (h, pqueue) = true} 
			    v : { v : int | true}   
                {\(h : heap), (v : int), (h' : heap). 
				        \(P : pq).
	                  v = pqlen (P) /\
                    [h' = h]
                };
       

find_min :  (pqueue : ref pq) ->  
              State 
                {\(h : heap).\(P : pq).
                    pqdom (h, pqueue) = true /\
                    (pqsel (h, pqueue) = P => 
                      pqlen (P) > 0)
                } 
			          v : { v : int| true}   
                {\(h : heap), (v : a), (h' : heap). 
				          \(P : pq), (P' : pq).
	                  v = minimum (P) /\
                    pqmem (P', v) = true /\ 
                    [h' = h]
                    };
       
  



find_min_exc : (pqueue : ref pq) ->  
              State 
                {\(h : heap). \(P : pq).
                    pqdom (h, pqueue) = true /\
                    (pqsel (h, pqueue) = P => pqlen (P) > 0)
                } 
			          v : { v : int| true}   
                {\(h : heap), (v : a), (h' : heap). 
				          \(P : pq), (P' : pq).
	                  v = minimum (P) /\
                    pqmem (P', v) = true /\ 
                    [h' = h]
                    };
       
delete_min :  (pqueue : ref pq) ->  
                State {\(h : heap). 
                    \(P : pq).
                    pqdom (h, pqueue) = true /\
                    (pqsel (h, pqueue) = P => 
                      pqlen (P) > 0)
                    } 
			    v : { v : unit | true}   
                {\(h : heap), (v : unit), (h' : heap). 
				          \(P : pq), (P' : pq), (A : int.
	                    pqsel (h, pqueue) = P /\
                      pqsel (h', pqueue) = P' /\
                      minimum (P) = A /\
                      pqmem (P', A) = false /\
                      pqlen (P') == pqlen (P) -- 1 
                  };
  
extract_min :  (pqueue : ref pq) ->  
                State {\(h : heap). 
                    \(P : pq).
                    pqdom (h, pqueue) = true /\
                    (pqsel (h, pqueue) = P => 
                      pqlen (P) > 0)
                    } 
			    v : { v : int | true}   
                {\(h : heap), (v : a), (h' : heap). 
				          \(P : pq), (P' : pq).
	                    pqsel (h, pqueue) = P /\
                      pqsel (h', pqueue) = P' /\
                      minimum (P) = v /\
                      pqmem (P', v) = false /\
                      pqlen (P') == pqlen (P) -- 1 
                  };
  
insert :    (x : a) -> 
            (pqueue : ref pq) -> 
             State {\(h : heap). 
                    \(P : pq).
                    pqdom (h, pqueue) = true} 
			            v : { v : unit | true}   
                {\(h : heap), (v : unit), (h' : heap). 
				          \(P : pq), (P' : pq).
	                    pqsel (h, pqueue) = P /\
                      pqsel (h', pqueue) = P' /\
                      pqmem (P', x) = true /\
                      (minimum (P) > x  => 
                          minimum (P') = x) /\
                      (not (minimum (P) > x)  => 
                           minimum (P') = minimum (P))
                               
                };
   
goal :  (x : int)  -> 
        (pqueue : ref pq) -> 
            State {\(h : heap). 
                    \(P : pq).
                    pqdom (h, pqueue) = true} 
			            v : { v : int | true}   
                {\(h : heap), (v : a), (h' : heap). 
				          \(P : pq), (P' : pq).
	                    (
                      pqsel (h, pqueue) = P /\
                      pqsel (h', pqueue) = P')
                      => 
                      (pqmem (P', x) = true /\
                        (minimum (P) > x  => [v = x]) /\
                       (not minimum (P) > x  => 
                           not [v = x])
                      )    
                };



type queue; 
qualifier qdom : heap :-> ref queue :-> bool;
qualifier vqmem : queue :-> a :-> bool;
qualifier qsel : heap :-> ref queue :-> queue;
qualifier qlen : queue :-> int;

create : State {\(h : heap). true} 
			v : ref queue 
		{ \(h : heap), (v : ref queue), (h' : heap). 
				\(Q' : queue).
		     qdom (h', v) = true  /\
                   qsel (h', v) = Q' /\ qlen (Q') = 0
              };



push :  (x : a) -> 
        (q : ref queue)  -> 
         State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q) = true
                 } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
			\(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    vqmem (Q1', x) = true /\
                    qlen (Q1') == qlen (Q1) + 1
                };


take :  (q : ref queue)  -> 
         State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q) = true /\
                        (qsel (h, q) = Q1 => qlen (Q1) > 0) 
                 } 
			     v : { v : a | true} 
                {\(h : heap), (v : a), (h' : heap). 
				 \(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    vqmem (Q1, v) = true /\
                    qlen (Q1') == qlen (Q1) -- 1
                };

pop : (q : ref queue)  -> 
         State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q) = true /\
                        (qsel (h, q) = Q1 => 
                        qlen (Q1) > 0) 
                 } 
			     v : { v : a | true} 
                {\(h : heap), (v : a), (h' : heap). 
				 \(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    vqmem (Q1, v) = true /\
                    vqmem (Q1', v) = false /\
                    qlen (Q1') == qlen (Q1) -- 1
                };
peek : (q : ref queue)  -> 
         State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q) = true /\
                        (qsel (h, q) = Q1 => 
                        qlen (Q1) > 0) 
                 } 
			     v : { v : a | true} 
                {\(h : heap), (v : a), (h' : heap). 
				 \(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    qlen (Q1') = qlen (Q1) /\
                    vqmem (Q1', q) = true 
                };

top : (q : ref queue)  -> 
         State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q) = true /\
                        (qsel (h, q) = Q1 => 
                        qlen (Q1) > 0) 
                 } 
			     v : { v : a | true} 
                {\(h : heap), (v : a), (h' : heap). 
				 \(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    qlen (Q1') = qlen (Q1) /\
                    vqmem (Q1', q) = true 
                };


clear : (q : ref queue) ->  
            State {\(h : heap). qdom (h, q) = true } 
			 v : { v : unit | true}    
             {\(h : heap), (v : unit), (h' : heap). 
				    \(Q : queue), (Q' : queue).
	                qsel (h, q) = Q /\    
                    qsel (h', q) = Q' /\ 
                    qlen (Q') = 0 
            };


copy : (q1 : ref queue) -> 
            State {\(h : heap).
                \(Q1: queue). 
                        qdom (h, q1) = true
                 } 
			     v : { v : ref queue | true} 
                {\(h : heap), (v : ref queue), (h' : heap). 
				 \(Q1: queue), (QN : queue). 
                    qsel (h, q1) = Q1 /\ 
                    qsel (h', v) = QN /\
                    qsel (h', q1) = qsel (h, q1) /\
                    qlen (QN) = qlen (Q1) 
                };


is_empty : (q : ref queue) ->  
                State {\(h : heap). 
                     qdom (h, q) = true} 
			    v : { v : bool | true}   
                {\(h : heap), (v : bool), (h' : heap). 
				    \(Q : queue), (Q' : queue).
	                  qsel (h, q) = Q /\
                      ([v = true] <=> qlen (Q) = 0) /\ 
                      ([v = false] <=> not (qlen (Q) = 0)) /\ 
                      [h' = h]
                    };


contains : (q : ref queue) ->  
             (x : a) -> 
                State {\(h : heap).\(Q : queue). 
                     qdom (h, q) = true /\
                     (qsel (h, q) = Q => qlen (Q) > 0)} 
			    v : { v : bool | true}   
                {\(h : heap), (v : bool), (h' : heap). 
			\(Q : queue), (Q' : queue).
	              qsel (h, q) = Q /\
                      ([v = true] <=> vqmem (Q, x) = true) /\ 
                      ([v = false] <=> vqmem (Q, x) = false) /\ 
                      [h' = h]
                    };


length :  (q : ref queue) ->  
                State {\(h : heap). 
                            qdom (h, q) = true} 
			    v : { v : int | true}   
                {\(h : heap), (v : int), (h' : heap). 
				\(Q : queue).
	              v = qlen (Q) /\
                     [h' = h]
                    };
       


add : (x : a) -> 
      (q : ref queue)  -> 
       State {\(h : heap).qdom (h, q) = true
                 } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit), (h' : heap). 
				 \(Q1: queue), (Q1' : queue). 
                    qsel (h, q) = Q1 /\ 
                    qsel (h', q) = Q1' /\
                    vqmem (Q1', x) = true /\
                    qlen (Q1') == qlen (Q1) + 1 /\
                    qdom (h', q) = true 
                };


transfer : (q1 : ref queue) -> 
           (q2 : ref queue) -> 
            State {\(h : heap).
                     qdom (h, q1) = true /\ 
                     qdom (h, q2) = true /\
                     not [q1 = q2]
                 } 
			     v : { v : unit | true} 
                {\(h : heap), (v : unit ), (h' : heap). 
				 \(Q1: queue), (Q2 : queue), (Q1' : queue), (Q2' : queue). 
                    qsel (h, q1) = Q1 /\ 
                    qsel (h', q1) = Q1' /\
                    qsel (h, q2) = Q2 /\
                    qsel (h', q2) = Q2' /\
                    qlen (Q2') == (qlen (Q1) + qlen (Q2)) /\
                    qlen (Q1') = 0 /\
                    not [q1 = q2]
                };

goal : (x : a) -> 
              State {\(h : heap). true} 
			v : ref queue 
		{ \(h : heap), (v : ref queue), (h' : heap). 
		       \(Q' : queue).
		       qdom (h', v) = false  /\
                     (qsel (h', v) = Q' => 
                     (qlen (Q') = 1 /\ 
                     vqmem (Q', x) = true))
              };


(*Ring Buffer*)
type buffer; 
qualifier rdom : heap :-> ref buffer :-> bool;
qualifier rmem : buffer :-> a :-> bool;
qualifier rsel : heap :-> ref buffer :-> buffer;
qualifier rlen : buffer :-> int;
qualifier rdisjoint : buffer :-> buffer :-> bool;

Max : int;

create: (capacity : { v : int | ([v > 0] \/ [v=0]) /\ not [Max > v]}) -> 
        (dummy : a) -> 
       	State {\(h : heap). true} 
			v : ref buffer 
		{ \(h : heap), (v : ref buffer), (h' : heap). 
				\(V : buffer), (V' : buffer).
		  rdom (h, v) = false /\
                  rdom (h', v) = true /\
                  rsel (h', v) = V' /\
                  rmem (V', dummy) = true /\
                  rlen (V') = 0
        };



length :  (vec : ref buffer) ->  
                State {\(h : heap). rdom (h, vec) = true} 
			    v : { v : int | true}   
                {\(h : heap), (v : int), (h' : heap). 
			\(V : buffer).
	                  v = rlen (V) /\
                         [h' = h]
                    };
       



clear : (vec : ref buffer) ->  
            State {\(h : heap). rdom (h, vec) = true} 
			 v : { v : unit | true}    
             {\(h : heap), (v : unit), (h' : heap). 
				    \(V : buffer), (V' : buffer).
	                rsel (h, vec) = V /\    
                    rsel (h', vec) = V' /\ 
                    rlen (V') = 0 
            };


pop : (a1 : ref buffer)  -> 
       State {\(h : heap).
                \(V1: buffer). 
                        rdom (h, a1) = true
                 } 
			     v : { v : a | true} 
                {\(h : heap), (v : a), (h' : heap). 
				 \(V1: buffer), (V1' : buffer). 
                    rsel (h, a1) = V1 /\ 
                    rsel (h', a1) = V1' /\
                    rmem (V1', v) = false /\
                    rlen (V1') = rlen (V1) - 1
                };



get : (vec : ref buffer) -> 
        (n : int) ->  
           State {\(h : heap).
                        \(V: buffer). 
                        rdom (h, vec) = true /\ 
                        (rsel (h, vec) = V => 
                        rlen (V) > n)
                } 
			    v : { v : a | true}   
                {\(h : heap), (v : a), (h' : heap). 
				    \(V : buffer).
	                rsel (h, vec) = V /\
                        rdom (V, v) = true /\ 
                        [h' = h]
                };


copy : (a1 : ref buffer) -> 
            State {\(h : heap).
                \(V1: buffer). 
                        rdom (h, a1) = true
                 } 
			     v : { v : ref buffer | true} 
                {\(h : heap), (v : ref buffer), (h' : heap). 
				 \(V1: buffer), (VN : buffer). 
                    rdom (h', v) = true /\
                    rsel (h, a1) = V1 /\ 
                    rsel (h, v) = VN /\
                    rsel (h', a1) = rsel (h, a1) /\
                    [VN = V1] /\
                    rlen (VN) = rlen (V1) /\
                    rdisjoint (V1, VN) = true 
                    
                };

goal : (a1 :  ref buffer) ->   
        State {\(h : heap). rdom (h, a1) = true} 
			v : ref buffer 
		{ \(h : heap), (v : ref buffer), (h' : heap). 
		\(V1 : buffer), (VN : buffer).
		  rdom (h', v) = true /\
                  (rsel (h, a1) = V1 /\ 
                  rsel (h, v) = VN ) => 
                  
                  (rsel (h', a1) = rsel (h, a1) /\
                  [VN = V1] /\
                  rlen (VN) = rlen (V1) /\
                  rdisjoint (V1, VN) = true) 
                 
        };

(*SLL*)
type cell;
type node;
qualifier lldom : heap :-> cell :-> bool;
qualifier llsel : heap :-> cell :-> node;
qualifier cons : node :-> bool;
qualifier content : node :-> a;
qualifier next : node :-> cell;
qualifier numcell : heap :-> int;


null : cell;
N : node;

create_cell : (c : cell) -> 
                State {\(h : heap). numcell (h) == 0}  
			v : {v : cell | true}  
		
                {\(h : heap), (v : cell), (h' : heap). 
				\(N' : node).
                   lldom (h', v) = true /\
                   llsel (h', v) = N' /\             
		            cons(N') = false /\
                   next (N') = null /\
                   numcell(h') == numcell(h) + 1
                  
        }; 

create_new_cell : (c : cell) -> 
                 State {\(h : heap). 
                \(N : node).
                        numcell (h) == 0 /\    
                        lldom (h, c) = true} 
			v : {v : cell | true}  
		{\(h : heap), (v : cell), (h' : heap). 
				\(N' : node).
                   lldom (h', v) = true /\
                   llsel (h', v) = N' /\             
		           cons(N') = false /\
                   next (N') = null /\
                   not [v = c] /\
                   numcell(h') == numcell(h) + 1
                  
        }; 



clear_cell : (c : cell) -> 
                 State {\(h : heap). \(N : node). 
                        lldom (h, c) = true /\ 
                        (llsel (h, c) = N => next (N) = null)} 
			v : {v : unit | true}  
		{\(h : heap), (v : unit), (h' : heap). 
				\(N' : node).
                   lldom (h', c) = false /\
                   [c = null] /\
                   numcell (h') == numcell (h) -- 1
        }; 

get_content : (c : cell) -> 
        State {\(h : heap). 
                \(N : node).
                lldom (h, c) = true /\
                (llsel (h, c) = N => cons (N) = true)} 
			v : {v : a | true}  
		{\(h : heap), (v : a), (h' : heap). 
				\(N' : node).
                   llsel (h, c) = N /\             
		   llsel (h', c) = llsel (h, c) /\ 
                  v = content (N') /\
                  numcell (h') == numcell (h)
                  
        };
 
set_next : (c : {v : cell | not (v = null)} ) ->
            (n : {v : cell| not (v = null) }) ->
               (data : a) -> 
        State {\(h : heap).         
                \(N : node).
                not [n= null] /\ 
                not [c=null] /\
                lldom (h, c) = true /\
                lldom (h, n) = true /\
                not [n=c] /\
                (llsel (h, c) = N => cons (N) = false) 
                 } 
				v : {v : unit | true}
		{\(h : heap), (v : unit), (h' : heap). 
				\(N' : node), (N : node).
		  llsel (h', c) = N' /\
                  llsel (h, c) = N /\
                  next (N') = n /\
                  content (N') = content (N) /\
                  cons (N') = true /\
                  numcell (h') == numcell (h)
        };       

set_content : (c : cell) ->
               (data : a) -> 
        State {\(h : heap).         
                \(N : node).
                lldom (h, c) = true /\
                (llsel (h, c) = N => cons (N) = true)} 
				v : {v : unit | true}
		{\(h : heap), (v : unit), (h' : heap). 
				\(N' : node), (N : node).
			      llsel (h', c) = N' /\
                  llsel (h, c) = N /\
                  content (N') = data /\
                  next (N') = next (N) /\
                  cons (N') = true /\
                  numcell (h') == numcell (h)
        };



get_next : (c : cell) -> 
         State {\(h : heap). 
                \(N : node).
                lldom (h, c) = true /\
                (llsel (h, c) = N => (cons (N) = true))} 
			v : {v : cell | true} 
		{\(h : heap), (v : cell), (h' : heap). 
				\(N' : node).
			      llsel (h', c) = N' /\
                  llsel (h', c) = llsel (h, c) /\ 
                  v = next (N') /\
                  numcell (h') == numcell (h)

        };


goal : (c : cell) ->
       (data : a) -> 
        State {\(h : heap).         
                \(N : node).
                lldom (h, c) = true /\
                llsel (h, c) = N /\ 
                cons (N) = true} 
			v : {v : unit | true}
		{\(h : heap), (v : unit), (h' : heap). 
				\(N' : node), (N : node).
		  (llsel (h',c) = N' /\
                  llsel (h, c) = N ) => 
                  content (N') = data /\
                  cons (N') = true /\
                  numcell (h') == numcell (h)
        };

