
- name: applyNtimes
query: "(a->a) -> a -> Int -> a"
solution: GHC.List.foldr Prelude.app x (GHC.List.replicate n f)
source: "hoogle"


stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> a -> Int -> a",
"inExamples": [],
"inArgNames": ["f","g","x"]}'




stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> a -> Int -> a",
"inExamples": [{"inputs": ["\\x -> x + 1","2", "2"],
                "output" : "5"
                }],
"inArgNames": ["f","g","x"]}'



stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> a -> Int -> a",
"inExamples": [{"inputs": ["\\x -> x ++ x", "f-", "3"],
              "output": \"f-f-f-f-f-f-f-f-\"}],
"inArgNames": ["f","g","y"]}'


(* Refined Query *)
goal = ??
