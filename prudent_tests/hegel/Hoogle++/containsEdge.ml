
(* Original O6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [],
"inArgNames": ["x", "y"]}'
(* E6_2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [{ "inputs": [ "[1,2,3]", "(2,3)"], 
                "output": "True"},
                { "inputs": [ "[1,2,3]", "(2,4)"], 
                "output": "False"}],
                "inArgNames": ["x", "y"]}'


(* E6_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [{ "inputs": [ "[1,2,3]", "(2,3)"], 
                "output": "True"},
                { "inputs": [ "[1,2,3]", "(2,4)"], 
                "output": "False"}],
                "inArgNames": ["x", "y"]}'
                
(* E6_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [{ "inputs": [ "[1,2,3]", "(2,3)"], 
                "output": "True"},
                { "inputs": [ "[1,2,3]", "(2,4)"], 
                "output": "False"}],
                "inArgNames": ["x", "y"]}'                


(* R6 *)
goal : (xs : int) -> y : (int, int) -> {v : bool | [v=true] <=> mem (fst (y), xs) = true /\
 mem (snd (y), xs) = true };


 (* output *)
