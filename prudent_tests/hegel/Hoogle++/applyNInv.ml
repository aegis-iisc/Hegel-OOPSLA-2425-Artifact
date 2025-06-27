
(* Inverse-Filter
(a → b) → (b -> a) → [a] -> [a]*)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [],
"inArgNames": ["f","x"]}'

(* Original *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [],
"inArgNames": ["h","f","g","xs"]}'


(* Refined2 *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> Bool) -> (a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [{"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 0]"],
              "output": "[5]"},
              {"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 4, 0]"],
              "output": "[5,4]"}],
"inArgNames": ["h", "f","g","xs"]}'


(* Refined4 *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> Bool) -> (a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [{"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 0]"],
              "output": "[5]"},
              {"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 4, 0]"],
              "output": "[5,4]"}],
"inArgNames": ["h", "f","g","xs"]}'



(* Refined6 *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> Bool) -> (a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [{"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 0]"],
              "output": "[5]"},
              {"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 4, 0]"],
              "output": "[5,4]"}],
"inArgNames": ["h", "f","g","xs"]}'



(* Refinement type *)
