- ApplyNAdd 
stack exec -- hplus --disable-filter=False --json='
{"query": "(Int->Int) -> Int -> Int -> Int -> Int",
"inExamples": [],
"inArgNames": ["f","init","n","add"]}'




stack exec -- hplus --disable-filter=False --json='
{"query": "(Int->Int) -> Int -> Int -> Int -> Int",
"inExamples": [{"inputs": ["\\x -> x + 1","0", "2", "3"],
              "output": "5"}],
"inArgNames": ["f","init","n","add"]}'



stack exec -- hplus --disable-filter=False --json='
{"query": "(Int->Int) -> Int -> Int -> Int -> Int",
"inExamples": [{"inputs": ["\\x -> x + 2","2", "3", "4"],
              "output": "12"},
              {"inputs": ["\\x -> x + 1","0", "2", "3"],
              "output": "5"}],
"inArgNames": ["f","init","n","add"]}'


(* Refinement type *)


goal p : (f : (x : int) -> { v : int | p (v) = true}) -> 
      (n : int) -> 
      (m : int) -> 
      (fuel :  { v : int | v = n}) -> 
      {v : int | fuel = 0 /\ p (v-m) = true}  


goal p : (f : (x : int) -> { v : int | p (v) = true}) -> 
        (n : int) -> 
        (m : int) -> 
        (fuel :  { v : int | v = n}) -> 
        {v : int | fuel = -1 /\ p (v-m) = true}  
  


  goal p : (f : (x : int) -> { v : int | p (v) = true}) -> 
          (n : int) -> 
          (m : int) -> 
          (fuel :  { v : int | v = n}) -> 
          {v : int | fuel = -1 /\ p (v-m) = true}  
            
  
        
  

