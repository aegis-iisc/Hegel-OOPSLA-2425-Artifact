(* <!-- NthIncr --> *)
(* O6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> a", 
"inExamples": [],
"inArgNames": ["x", "y"]}'


(* E6_2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[Int] -> Int", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "2"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'



(* E6_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[Int] -> Int", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "2"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'



(* E6_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[Int] -> Int", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "2"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'

(* <!-- R6 --> *)
goal : (x : Int) -> (xs : [Int]) -> 
  {v : Int |  \(u : Int). (sel (xs, x) = u) => v = u + 1 };
  


(* Output *)