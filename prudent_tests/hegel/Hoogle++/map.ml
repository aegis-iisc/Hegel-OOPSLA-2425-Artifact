(* name : mapApply and rotate *)
(* Original Query *)
stack exec -- hplus --disable-filter=False --json='{"query": "(a->b)->[a]->[b]",
"inExamples": [],
"inArgNames": ["f","x"]}'


(* Original Monomorphic query *)
stack exec -- hplus --disable-filter=False --json='{"query": "(Int -> Int) -> [Int]->[Int]",
  "inExamples": [],
  "inArgNames": ["x"]}'



(* E2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "(Int -> Int) -> [Int]->[Int]",
  "inExamples": [{ "inputs": ["\\x -> x+1", "[1,0,4,8]"],
                    "output": "[9,5,1,2]"},
                    { "inputs": ["\\x -> x", "[1,0,4,8]"],
                    "output": "[8,4,0,1]"}], 
  "inArgNames": ["f","x"]}'



(*Refinement Type *)
  goal p : (f : (x : int) -> { v : int | p}) -> 
                      (l : [int]) -> {v : [int] | \(u : int). mem (u , v) = true => 
                            p (u-1) }

  goal p : (f : (x : int) -> { v : int | p v}) -> 
                              (l : [int]) -> {v : [int] | \(u : int). mem (u , v) = true => 
                                    p (u+1) }

 goal p : (f : (x : int) -> { v : int | p v}) -> 
            (l : [int]) -> {v : [int] | \(u : int). mem (u , v) = true => 
                                            p (u-1) /\ 
                                          \(u1 : int), (u2 : int). order (u1, u2, l) = true => 
                                          u1' = u1 - 1 /\ u2' = u2 - 1
                                          order (u1', u2', v) = true}
        
