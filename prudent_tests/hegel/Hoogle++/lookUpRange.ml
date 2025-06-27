
(* <!-- 18 lookupC *)
(* Eq a => [(a,b)] -> a -> b --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [],
"inArgNames": ["x", "y"]}'

stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [],
"inArgNames": ["x", "y"]}'


<!-- Examples -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "3"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "3"], 
                "output": "4"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "5"], 
                "output": "6"}
                ],
"inArgNames": ["x", "y"]}'

<!-- Suceeds -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "3"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "3"], 
                "output": "4"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "5"], 
                "output": "6"}
                ],
"inArgNames": ["x", "y"]}'


<!-- Fails -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5, 6)]", "3"], 
                "output": "2"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "1"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "6"], 
                "output": "5"}
                ],
"inArgNames": ["x", "y"]}'
<!-- Fails -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5, 6)]", "3"], 
                "output": "2"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "1"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "6"], 
                "output": "5"}
                ],
"inArgNames": ["x", "y"]}'

(* lookUpRange for a given function *)
goal = (l : [(a,b)]) -> (k : b) ->  -> {v : a | \(u: int). mem (u, k, l) = false => not (v = k)}

goal = (l : [(a,b)]) -> (k : b) ->  -> {v : a | \(u: a). snd (l) = s /\
                                        mem (u, k, l) = false => not (v = k) /\ 
                                        \(u1 : b). mem (u1, s) = true  /\  mem (u, k, l) = false => v = last (fst (l))}

goal = (l : [(a,b)]) -> (k : b) ->  -> {v : a | \(u: a). snd (l) = s /\
                                        mem (u, k, l) = false => not (v = k) /\ 
                                        \(u1 : b). mem (u1, s) = true  /\  mem (u, k, l) = false => v = hd (fst (l))}



