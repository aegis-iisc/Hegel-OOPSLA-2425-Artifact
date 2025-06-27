(* <!-- revZip , 
uses zip function, reverse the list and then try zip *)

(* <!-- O4, finds a solution --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [],
"inArgNames": ["x", "y"]}'

(* E3_2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* E3_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* E3_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* <!-- R3 --> *)
goal : (x : [a]) -> (y : [a]) -> 
{v : [pair] |  \(u : [a]), (w : a), (z : a). sndlist (v, u) = true => 
(mem (w, u) = true => mem (w, y) = true) /\ 
(ord (w, z, u) = true => ord (z, w, y))};

(* Output *)
zip x (reverse y)
