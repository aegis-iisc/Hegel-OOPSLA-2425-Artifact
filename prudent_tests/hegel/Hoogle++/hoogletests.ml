<!-- For each benchmark, we need 
the original query Oi
the example refined query Ei2, Ei4 and Ei6
the refinement type query Ri -->


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


------------------------------------------------------------------------------
(* <!-- query2 E2--> *)


(* <!-- Original O2 --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [], 
 "inArgNames": ["z"]}'


(* E2_2 *)
 stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [{ "inputs": ["[1,2,3,4]"], 
                "output": "[1,2,3,4,4,3,2,1]"},
                { "inputs": ["[1,3,5,6]"], 
                "output": "[1,3,5,6,6,5,3,1]"},
                { "inputs": ["[\"abcd\"]"], 
                "output": "[\"abcddcba\"]"}],
 "inArgNames": ["z"]}'



(* E2_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
"inExamples": [{ "inputs": ["[1,2,3,4]"], 
               "output": "[1,2,3,4,4,3,2,1]"},
               { "inputs": ["[1,3,5,6]"], 
               "output": "[1,3,5,6,6,5,3,1]"},
               { "inputs": ["[\"abcd\"]"], 
               "output": "[\"abcddcba\"]"}],
"inArgNames": ["z"]}'



(* E2_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
"inExamples": [{ "inputs": ["[1,2,3,4]"], 
               "output": "[1,2,3,4,4,3,2,1]"},
               { "inputs": ["[1,3,5,6]"], 
               "output": "[1,3,5,6,6,5,3,1]"},
               { "inputs": ["[\"abcd\"]"], 
               "output": "[\"abcddcba\"]"}],
"inArgNames": ["z"]}'

(* <!-- R2 
We just say that the size is doubled and the members remain the same.
if (a,b) in z then (b,a) in v
--> *)
goal : (z : [int]) -> 
    {v : [int] | \(u : int), (w : int). mem (u, v) = true => mem (u , z) /\
                        len (v) == len (z) +  len (z) /\
                        ord (u, w, z) = true => 
                        (ord (u, w, v) = true /\ ord (w, u, v) = true)
                        };



  (* Output *)

  ??
--------------------
<!-- Higher order query solution query3 -->

<!-- Refined E3 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [a] -> Int -> a", 
 "inExamples": [{ "inputs": ["[49,62,82,54,76]", "2"], 
                "output": "130"},
                { "inputs": ["[49,62,82,54,76]","3"], 
                "output": "212"},
                { "inputs": ["[49,62,82,54,76]","1"], 
                "output": "76"},
                { "inputs": ["[49,62,82,54,76]","4"], 
                "output": "274"}],
 "inArgNames": ["x", "y"]}'


<!-- Original O3-->

stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [a] -> Int -> a", 
 "inExamples": [],
 "inArgNames": ["x", "y"]}'



<!-- R3 
Defining sum in LH
This is hard to define precisely using refinements 

-->

goal : (x : [int]) -> 
    {v : [int] | \(u : int), (w : int). mem (u, v) = true => mem (u , z) = true /\
                        len (v) == len (z) +  len (z) /\
                        ord (u, w, z) = true => 
                        (ord (u, w, v) = true /\ ord (w, u, v) = true)
                        };




---------------
(* <!-- revZip , 
uses zip function, reverse the list and then try zip *)

(* <!-- O4, finds a solution --> *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [],
"inArgNames": ["x", "y"]}'

(* E3_2 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* E3_4 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* E3_6 *)
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'


(* <!-- R3 --> *)
goal : (x : [a]) -> (y : [a]) -> 
{v : [pair] |  \(u : [a]), (w : a), (z : a). sndlist (v, u) = true => 
(mem (w, u) = true => mem (w, y) = true) /\ 
(ord (w, z, u) = true => ord (z, w, y))};

(* Output *)



-----------------------------------

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
---------------------------

<!-- query6 Same as the summation of the list n elements query -->

<!-- E6 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [Int] -> Int -> Int", 
 "inExamples": [{ "inputs": ["[49,62,82,54,76]", "2"], 
                "output": "111"},
                { "inputs": ["[49,62,82,54,76]","3"], 
                "output": "193"},
                { "inputs": ["[1,3,5]","2"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'

<!-- O6, same as earlier sum case -->




query7
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[a] -> a", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "1"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "3"},
                { "inputs": ["3", "[\"abcd\"]"], 
                "output": "\"c\""}],
 "inArgNames": ["x", "y"]}'

stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[a] -> a", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "1"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "3"}],
 "inArgNames": ["x", "y"]}'
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
  {v : Int |  
      \(u : Int). (sel (xs, x) = u) => v = u + 1 };
  



--------------------------
appendNTimes
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> [a]", 
 "inExamples": [{ "inputs": ["2", "[1,2,3,4]"], 
                "output": "[1,2,3,4,1,2,3,4]"},
                { "inputs": ["3", "[1,3,5,6]"], 
                "output": "[1,3,5,6,1,3,5,6,1,3,5,6]"},
                { "inputs": ["4", "[\"abcd\"]"], 
                "output": "[\"abcdabcdabcdabcd\"]"}],
 "inArgNames": ["x", "z"]}'
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> [a]", 
 "inExamples": [],
 "inArgNames": ["x", "z"]}'



query9 rev
stack exec -- hplus --disable-filter=False --json='{"query":"[a] -> [a]", 
 "inExamples": [{ "inputs": ["[1,2,3,4]"], 
                "output": "[4,3,2,1]"},
                { "inputs": ["[1,3,5,6]"], 
                "output": "[6,5,3,1]"},
                { "inputs": ["[\"abcd\"]"], 
                "output": "[\"dcba\"]"}],
 "inArgNames": ["z"]}'
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [],
 "inArgNames": ["z"]}'


********************************** Hoogle+ Tests **************
name : test
stack exec -- hplus --disable-filter=False --json='{"query":"b: Bool -> x: a -> Maybe a", 
"inExamples": [{"inputs": ["True", "1"],
                "output": "Just 1" },
               {"inputs": ["False", "2"],
                  "output": "Nothing"}],
"inArgNames": ["b", "x"]}'
stack exec -- hplus --disable-filter=False --json='{"query":"b: Bool -> x: a -> Maybe a", 
"inExamples": [],
 "inArgNames": ["b", "x"]}'

stack exec -- hplus --disable-filter=False --json='{"query":"", 
"inExamples": [{"inputs": ["True", "1"],
                "output": "Just 1" },
               {"inputs": ["False", "2"],
                  "output": "Nothing"}]}'

 In this particular case, the synthesizer when run without examples, is able two synthesize 3 programs and then loops for around an hour to find 4 and 5 and fails.


name : firstJust 
--successful
stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> xs: [Maybe a] -> a",
"inExamples": [{"inputs": ["3", "[Nothing, Just 2, Nothing]"],
                "output": "2"},
                {"inputs": ["3", "[]"],
                "output": "3"}],
"inArgNames": ["x", "xs"]}'

--sucessful finds a different program
stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> xs: [Maybe a] -> a",
"inExamples": [],
"inArgNames": ["x", "xs"]}'

-- a modified program which returns a singleton list is gets stuck
stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> xs: [Maybe a] -> [a]",
"inExamples": [{"inputs": ["3", "[Nothing, Just 2, Nothing]"],
                "output": "[2]"},
                {"inputs": ["3", "[]"],
                "output": "[]"}],
"inArgNames": ["x", "xs"]}'

**************************************
- fails
name: mergeEither

stack exec -- hplus --disable-filter=False --json='{"query": "e: Either a (Either a b) -> Either a b",
"inExamples": [{"inputs": ["Left 2"],
                "output": "Left 2"},
                {"inputs": ["Right (Left 2)"],
                 "output": "Left 2"},
                {"inputs": ["Right (Right 2.2)"],
                "output": "Right 2.2"}],
"inArgNames": ["e"]}'
- successful case without example
stack exec -- hplus --disable-filter=False --json='{"query": "e: Either a (Either a b) -> Either a b",
"inExamples": [],
"inArgNames": ["e"]}'

******************************************


- name: singletonList
 
stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> [a]",
"inExamples": [{"inputs": ["2"], 
                "output": "[2]"},
               {"inputs": ["\"abc\""],
                 "output": "[\"abc\"]"}],
"inArgNames": ["x"]}'


stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> [a]",
"inExamples": [],
"inArgNames": ["x"]}'

*******modified query
stack exec -- hplus --disable-filter=False --json='{"query": "x: a -> [a]",
"inExamples": [{"inputs": ["2"], 
                "output": "[2,2]"},
               {"inputs": ["\"abc\""],
                 "output": "[\"abcabc\"]"}],
"inArgNames": ["x"]}'


*******************************************

name: headLast
stack exec -- hplus --disable-filter=False --json='{"query": "xs: [a] -> (a, a)",
"inExamples": [{"inputs": ["[1,2,3,4]"],
            "output": "(1, 4)"}],
"inArgNames": ["x"]}'



Key findings:

Research Question we are trying to solve
Is Hegel successful in finding solutions (efficiently) where Hoogle + refinement with examples finds is challenging. 
- Steps, I take each of the first-order query in Hoogle, add examples (takes the same examples they have) to find the solution.

Out of 14 different queries, in only 1 Hoogle+ found a solution in the given timebound.
For rest, the synthesizer did not terminate (timeout 1hr, trying 1 solution).

The reason for this, is that the synthesizer decouples the petrinet based synthesis with the example based filtering, and Petrinet based synthesis are not well guided towards a partiular goal, as as result, these

Out of these benchmarks, when considered the list libray of 14 functions, Cobalt finds a solution in average time for a small library

The evaluation, will go like this, for each of the Hoogle+ benchmarks, with the examples or added examples, we run TyGAR, Hoogle+, Cobalt and Prudent.

To evaluate the effectiveness of the Prudent, minimization algorithm, we disable minimization of the PTA, and compare it against the Propsynth.


To highlight, the effectiveness of incremental checking we have two modes, one complete queries vs one with incremental checking.

Finally, we have another set of becnhmarks, which is of larger  programs:
1. RedBlackTree
2. SizedBST
3. SizedList 
These programs cannot be solved using Hoogle+

- Implement the


A detailed analysis of the programs

SNo. are matching the Hoogle+ paper.
<!-- 
5 containsEdge
[Int] -> (Int,Int) -> Bool -->

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

---------------------------------------
<!-- 7 appendN
Int -> [a] -> [a] -->


<!-- Finds a solution 2 sec -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> [a]", 
"inExamples": [],
"inArgNames": ["x", "y"]}'


<!-- Succeeds in finding a solution. 15 sec -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> [a]", 
"inExamples": [{ "inputs": [ "2", "[1,2,3]"], 
                "output": "[1,2,3,1,2,3]"},
                { "inputs": [ "3", "[1,2,3]"], 
                "output": "[1,2,3,1,2,3,1,2,3]"}],
"inArgNames": ["n", "xs"]}'

<!-- Fails to find  a solution -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> [a]", 
"inExamples": [ { "inputs": [ "1", "[1,2,3]"], 
                "output": "[1,2,3,1]"},
                { "inputs": [ "2", "[1,2,3]"], 
                "output": "[1,2,3,1,2]"},
                { "inputs": [ "3", "[1,2,3]"], 
                "output": "[1,2,3,1,2,3]"}],
"inArgNames": ["n", "xs"]}'

(* <!-- Refinement type --> *)
goal : (x : int) -> (xs : [a]) -> { v : [a] | 
    \(u : a). mem (u, xs) = true => mem (u, v) = true /\ count (u, v) = size (v) = x};
(* appendsize : a :-> [a] :-> int
appendsize [] = 0 
appendsize (x :: xs) = 1

appned : x : [a] -> y : [a] -> {v : [a] | \(u : a). mem (u, x) = true => mem (u, v) /\
 mem (u, y) => mem (u, v) /\ mem (u, x) = true /\ appendsize (v) = appendsize (x) + appendsize (y)   
*)

----------------------------


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
goal = (s : string) -> (c : char) -> { v : (String, String) | ?? }



--------------------


<!-- 18 lookupC
Eq a => [(a,b)] -> a -> b -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [],
"inArgNames": ["x", "y"]}'

stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [],
"inArgNames": ["x", "y"]}'


<!-- Examples -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "3"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "3"], 
                "output": "4"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "5"], 
                "output": "6"}
                ],
"inArgNames": ["x", "y"]}'

<!-- Suceeds -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "3"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "3"], 
                "output": "4"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "5"], 
                "output": "6"}
                ],
"inArgNames": ["x", "y"]}'


<!-- Fails -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,b)] -> a -> b", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5, 6)]", "3"], 
                "output": "2"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "1"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "6"], 
                "output": "5"}
                ],
"inArgNames": ["x", "y"]}'
<!-- Fails -->
stack exec -- hplus --disable-filter=False --json='{"query": "Eq a => [(a,a)] -> a -> a", 
"inExamples": [{"inputs": ["[(1,2), (2,3), (3, 4), (5, 6)]", "3"], 
                "output": "2"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "2"], 
                "output": "1"},
                {"inputs": ["[(1,2), (2,3), (3, 4), (5,6)]", "6"], 
                "output": "5"}
                ],
"inArgNames": ["x", "y"]}'

<!-- Refinement type -->


goal = ??



************** Higher order functions************
(* name : map *)
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


(* E4 *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [{"inputs": ["\\x -> x + 1","\\y -> y + 1","[1,2,3,4]"],
              "output": "[3,4,5,6]"}],
"inArgNames": ["f","g","x"]}'

(*A larger query cannot be solved)*)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [],
"inArgNames": ["f","g","x"]}'

(*Refinement Type *)
goal : 
******************************************
(* DoubleMap *)

(* Original *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [],
"inArgNames": ["f","g","x"]}'


(* Double map application fails  *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [{"inputs": ["\\x -> x + 1","\\y -> y + 1","[1,2,3,4]"],
              "output": "[3,4,5,6]"}],
"inArgNames": ["f","g","x"]}'





(* E4 *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [{"inputs": ["\\x -> x + 1","\\y -> y + 1","[1,2,3,4]"],
              "output": "[3,4,5,6]"}],
"inArgNames": ["f","g","x"]}'

(*A larger query cannot be solved)*)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->b) -> (b -> a) -> [a]->[a]",
"inExamples": [],
"inArgNames": ["f","g","x"]}'


goal: 

----------------------------------------

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

---------------------------------------------
stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> ((a -> a) -> a -> Int -> a) -> a -> Int -> a",
"inExamples": [],
"inArgNames": ["f","g","x", "y"]}'


stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> a -> Int -> a",
"inExamples": [{"inputs": ["\\x -> x ++ x", "f-", "3"],
              "output": \"f-f-f-f-f-f-f-f-\"}],
"inArgNames": ["f","g","y"]}'


stack exec -- hplus --disable-filter=False --json='
{"query": "(a->a) -> a -> Int -> a",
"inExamples": [{"inputs": ["\\x -> x + 1","2", "3"],
              "output": "5"}],
"inArgNames": ["f","g","x"]}'

**********************************
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









******************************
-- ApplyListInvavriant
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [],
"inArgNames": ["f","x"]}'

--successful
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [{"inputs": ["[(\\x -> x + 2),(\\x -> x * 2)]","5"],
              "output": "[7,10]"}],
"inArgNames": ["f","x"]}'


-failed, apply the head of the function list to the argument

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



******************************
Look at some of the programs in Hoogle+/ECTA and work on the final example after the paper.

-- ApplyListInvavriant
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [],
"inArgNames": ["f","x"]}'

--successful
stack exec -- hplus --disable-filter=False --json='
{"query": "[(a->b)] -> a -> [b]",
"inExamples": [{"inputs": ["[(\\x -> x + 2),(\\x -> x * 2)]","5"],
              "output": "[7,10]"}],
"inArgNames": ["f","x"]}'


-failed, apply the head of the function list to the argument

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

***************************

(*Both 
(a → b) → (a, a) → (b, b) 
*)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (a, a) -> (b, b)",
"inExamples": [],
"inArgNames": ["f","x"]}'

(* Refined , apply the function just to the second argumentquery *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> a) -> (a, a) -> (a, a)",
"inExamples": [{"inputs": ["\\x -> 2*x","(5, 2)"],
              "output": "(4, 5)"},
              {"inputs": ["\\x -> x+1","(3, 1)"],
              "output": "(2, 3)"}],
"inArgNames": ["f","x"]}'

stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (a, a) -> (a, b)",
"inExamples": [{"inputs": ["\\x -> 2*x","(5, 2)"],
              "output": "(5, 4)"},
              {"inputs": ["\\x -> x+1","(3, 1)"],
              "output": "(3, 2)"}],
"inArgNames": ["f","x"]}'


(* solution
 (fst x, f (snd x))
 *)
(* Refinement Types *)
goal : <p : b :-> bool> (f : (a -> { v : b | p  v})) -> x : (a * a) -> { v : (a * a) | }



(* 
(a → b) → (b -> a) → [a] -> [a]*)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [],
"inArgNames": ["f","x"]}'

stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [],
"inArgNames": ["f","g","xs"]}'


(* Refined , apply the function just to the second argumentquery *)
stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [{"inputs": ["\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 0]"],
              "output": "[0, -1]"}],
"inArgNames": ["f","g","xs"]}'

stack exec -- hplus --disable-filter=False --json='
{"query": "(a -> Bool) -> (a -> b) -> (b -> a) -> [a] -> [a]",
"inExamples": [{"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 0]"],
              "output": "[5]"},
              {"inputs": ["\\x -> if (x >= 0) then True else False", "\\x -> if (x > 0) then True else False", "\\x -> if (x) then 0 else -1", "[5, 4, 0]"],
              "output": "[5,4]"}],
"inArgNames": ["h", "f","g","xs"]}'

(* Refinement type *)
