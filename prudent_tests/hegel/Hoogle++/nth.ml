
  (* -- O1 --by types only,, finds a solution *)
  stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
  "inExamples": [],
  "inArgNames": ["x", "y", "z"]}'
 
 Found solution: 
 \\arg0 arg1 arg2 -> GHC.List.drop arg0 (GHC.List.drop arg1 arg2)
 


(* <!-- --by both examples and types
-- example, get elements at position x and y and place it in the end of the input. --> *)

<!-- E1_2 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [{ "inputs": ["0", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,1,5]"},
                { "inputs": ["1", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,3,5]"},
                { "inputs": ["0", "2", "[\"abcd\"]"], 
                "output": "[\"abcdac\"]"}],
 "inArgNames": ["x", "y", "z"]}'

<!-- E1_4-->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
"inExamples": [{ "inputs": ["0", "2", "[1,3,5,6]"], 
              "output": "[1,3,5,6,1,5]"},
              { "inputs": ["1", "2", "[1,3,5,6]"], 
              "output": "[1,3,5,6,3,5]"},
              { "inputs": ["0", "2", "[\"abcd\"]"], 
              "output": "[\"abcdac\"]"}],
"inArgNames": ["x", "y", "z"]}'


<!-- E1_6 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [{ "inputs": ["0", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,1,5]"},
                { "inputs": ["1", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,3,5]"},
                { "inputs": ["0", "2", "[\"abcd\"]"], 
                "output": "[\"abcdac\"]"}],
 "inArgNames": ["x", "y", "z"]}'
(* 
Possible outputs:  *)
goal : (x:int) (y:int) (z : v : [int]) = 
reverse (z!!y : (z!!x : (reverse z)))
append ( z, 
cons ((z!!x),  singleton (z!!y))
) 

(* <!-- R1, a query for the Hegel --> *)
goal : (x:int) -> (y:int) -> z : {v : [int] | len (z) >= x /\ len (z) >= y} -> 
  {v : [int] | \(u : int). mem (u, v) = true => mem (u , z) /\
                      len (v) == len (z) + 2 /\
                      nth (x, z) = pen (v) /\
                      nth (y, z) = last (v)};

