(* --ApplyListInverse *)
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [],
"inArgNames": ["f","x"]}'

(* --successful *)
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [{"inputs": ["[(\\x -> x + 2),(\\x -> x * 2)]","5"],
              "output": "[7,10]"}],
"inArgNames": ["f","x"]}'


(* -failed, apply the head of the function list to the argument *)
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [{"inputs": ["[(\\x -> x + 2),(\\x -> x * 2)]","5"],
              "output": "[7]"}],
"inArgNames": ["f","x"]}'



stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [{"inputs": ["[(\\x -> x + 1),(\\x -> x + 2),(\\x -> x * 2)]","5"],
              "output": "[7,10]"}],
"inArgNames": ["f","x"]}'


(*  Refinement types*)




(* --successful *)
stack exec -- hplus --disable-filter=False --json='
{"query": "[(Int->Int)] -> Int -> [Int]",
"inExamples": [],
"inArgNames": ["f","x"]}'


(* fails *)
stack exec -- hplus --disable-filter=False --json='
{"query": "[(Int->Int)] -> Int -> [Int]",
"inExamples": [{"inputs": ["[(\\x -> 2*x),(\\x -> 3*x)]","5"],
              "output": "[10,15]"}],
"inArgNames": ["f","x"]}'


stack exec -- hplus --disable-filter=False --json='
{"query": "[(Int->Int)] -> Int -> [Int]",
"inExamples": [{"inputs": ["[(\\x -> if (x > 10) then 10 else 10),(\\x -> 9)]","5"],
              "output": "[10,9]"}],
"inArgNames": ["f","x"]}'




(* refinement types *)
goal : (fs : {v : [Int -> Int] | \(u : Int -> Int). mem (u, v) => ltten (v)}) -> (x : Int) -> 
{v : [Int] | \(u : Int). mem (u, v) => u <= 10};  