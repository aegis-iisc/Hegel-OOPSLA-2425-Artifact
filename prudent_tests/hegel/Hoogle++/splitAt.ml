
(* <!-- query5, the motivational example from the paper --> *)

(* <!-- E5  --> 
  splitAt from the paper 
  *)


(* <!-- O5 --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
 "inExamples": [],
 "inArgNames": ["x", "y", "z"]}'

(*  E5_2 *)
 stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
 "inExamples": [{ "inputs": ["1", "2", "[49, 62, 82, 54, 76]"], 
                "output": "([49],[82,54,76])"},
                { "inputs": ["2", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49,62],[54,76])"},
                { "inputs": ["3", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49, 62, 82],[54, 76])"}],
 "inArgNames": ["x", "y", "z"]}'

(*  E5_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
"inExamples": [{ "inputs": ["1", "2", "[49, 62, 82, 54, 76]"], 
               "output": "([49],[82,54,76])"},
               { "inputs": ["2", "3", "[49, 62, 82, 54, 76]"], 
               "output": "([49,62],[54,76])"},
               { "inputs": ["3", "3", "[49, 62, 82, 54, 76]"], 
               "output": "([49, 62, 82],[54, 76])"}],
"inArgNames": ["x", "y", "z"]}'

(*  E5_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
"inExamples": [{ "inputs": ["1", "2", "[49, 62, 82, 54, 76]"], 
               "output": "([49],[82,54,76])"},
               { "inputs": ["2", "3", "[49, 62, 82, 54, 76]"], 
               "output": "([49,62],[54,76])"},
               { "inputs": ["3", "3", "[49, 62, 82, 54, 76]"], 
               "output": "([49, 62, 82],[54, 76])"}],
"inArgNames": ["x", "y", "z"]}'

<!-- R5, the refinement type from the paper  -->
goal : (x:int) 
-> (y : int) 
-> (xs : [a]) 
-> { v : ([a], [a]) | 
len (fst (v)) <= x 
/\ (len (snd (v)) $<=$ len (xs) - y \/ len (snd (v) = 0)) 
/\ \(u : a). mem (fst (v). u) = true => mem (xs, u) 
/\ \(u : a). mem (snd (v), u) = true => mem (xs, u)};

(* output *)