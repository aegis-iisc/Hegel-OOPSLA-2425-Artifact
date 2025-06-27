(* <!-- query2 E2--> *)


(* <!-- Original O2 --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [], 
 "inArgNames": ["z"]}'


(* E2_2 *)
 stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [{ "inputs": ["[1,2,3,4]"], 
                "output": "[1,2,3,4,4,3,2,1]"},
                { "inputs": ["[1,3,5,6]"], 
                "output": "[1,3,5,6,6,5,3,1]"},
                { "inputs": ["[\"abcd\"]"], 
                "output": "[\"abcddcba\"]"}],
 "inArgNames": ["z"]}'



(* E2_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
"inExamples": [{ "inputs": ["[1,2,3,4]"], 
               "output": "[1,2,3,4,4,3,2,1]"},
               { "inputs": ["[1,3,5,6]"], 
               "output": "[1,3,5,6,6,5,3,1]"},
               { "inputs": ["[\"abcd\"]"], 
               "output": "[\"abcddcba\"]"}],
"inArgNames": ["z"]}'



(* E2_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
"inExamples": [{ "inputs": ["[1,2,3,4]"], 
               "output": "[1,2,3,4,4,3,2,1]"},
               { "inputs": ["[1,3,5,6]"], 
               "output": "[1,3,5,6,6,5,3,1]"},
               { "inputs": ["[\"abcd\"]"], 
               "output": "[\"abcddcba\"]"}],
"inArgNames": ["z"]}'

(* <!-- R2 
We just say that the size is doubled and the members remain the same.
if (a,b) in z then (b,a) in v
--> *)
goal : (z : [int]) -> 
    {v : [int] | \(u : int), (w : int). mem (u, v) = true => mem (u , z) /\
                        len (v) == len (z) +  len (z) /\
                        ord (u, w, z) = true => 
                        (ord (u, w, v) = true /\ ord (w, u, v) = true)
                        };



  (* Output *)
concat z (reverse z)