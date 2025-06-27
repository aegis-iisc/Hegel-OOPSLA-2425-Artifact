
(* 17 splitStr String -> Char -> [String] *)


(* Original *)
stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> (String, String)", 
"inExamples": [],
"inArgNames": ["x", "y"]}'

(* E2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> (String, String)", 
"inExamples": [{ "inputs": ["\"abc\"", "\'b\'" ], 
                "output": "["\"ab\"", "\"c\"""},
                {"inputs": ["\"abcd\"", "\'c\'", 
                "output": "["\"abc\"", "\"d\""}],
"inArgNames": ["x", "y"]}' 




stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> (String, String)", 
"inExamples": [{ "inputs": ["\"abc\"", "\'b\'" ], 
                "output": "["\"ab\"", "\"c\""},
                {"inputs": ["\"abcd\"", "\'c\'"], 
                "output": "["\"abc\"", "\"d\""}],
"inArgNames": ["x", "y"]}'


(* E6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> [String]", 
"inExamples": [{ "inputs": ["\"abc\"", "\'b\'" ], 
                "output": "["\"ab\"", "\"c\"" }],
"inArgNames": ["x", "y"]}'


(* <!-- Refinement types --> 
 Treast Strings as list of chars  
  *)
goal = (s : string) -> (c : char) -> { v : (String, String) |
                                      f = fst (v) /\ sn = snd (v) /\
                                       mem (c, f) = true  /\
                                \(u : char). mem (u, f) = true => mem (u , s) /\
                                \(u : chat). mem (u, sn) = true => mem (u, s) }

goal = (s : string) -> (c : char) -> { v : (String, String) |
                                f = fst (v) /\ sn = snd (v) /\
                                 mem (c, f) = true  /\
                          \(u : char). mem (u, f) = true => mem (u , s) /\
                          \(u : char). mem (u, sn) = true => mem (u, s) /\
                          \(u : char), (u1 : char). order (u, u1, s) => order (u1, u, sn) }

goal = (s : string) -> (c : char) -> { v : (String, String) |
                          f = fst (v) /\ sn = snd (v) /\
                           mem (c, sn) = true  /\
                    \(u : char). mem (u, f) = true => mem (u , s) /\
                    \(u : chat). mem (u, s) = true => mem (u, s) }
