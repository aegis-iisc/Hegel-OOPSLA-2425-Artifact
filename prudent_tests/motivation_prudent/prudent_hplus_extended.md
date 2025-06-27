<!-- (*Uses the most recent example of the prudent.md file*) -->
<!-- For each benchmark, we need 
the original query Oi
the example refined query Ei
the refinement type query Ri
 -->

query1.

<!-- --by both examples and types
-- example, get elements at position x and y and place it in the end of the input. -->

<!-- E1 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [{ "inputs": ["0", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,1,5]"},
                { "inputs": ["1", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,3,5]"},
                { "inputs": ["0", "2", "[\"abcd\"]"], 
                "output": "[\"abcdac\"]"}],
 "inArgNames": ["x", "y", "z"]}'

<!-- Possible outputs: 
reverse (z!!y : (z!!x : (reverse z)))

append ( z, 

cons ((z!!x),  singleton (z!!y))
) -->

<!-- R1, a query for the Hegel -->
goal : (x:int) -> (y:int) -> z : {v : [int] | len (z) >= x /\ len (z) >= y} -> 
    {v : [int] | \(u : int). mem (u, v) = true => mem (u , z) /\
                        len (v) == len (z) + 2 /\
                        nth (x, z) = pen (v) /\
                        nth (y, z) = last (v)};

 <!-- O1 --by types only,, finds a solution -->
 stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [],
 "inArgNames": ["x", "y", "z"]}'

Found solution: 
\\arg0 arg1 arg2 -> GHC.List.drop arg0 (GHC.List.drop arg1 arg2)

------------------
<!-- query2 E2-->
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [{ "inputs": ["[1,2,3,4]"], 
                "output": "[1,2,3,4,4,3,2,1]"},
                { "inputs": ["[1,3,5,6]"], 
                "output": "[1,3,5,6,6,5,3,1]"},
                { "inputs": ["[\"abcd\"]"], 
                "output": "[\"abcddcba\"]"}],
 "inArgNames": ["z"]}'

<!-- Original O2 -->
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [], 
 "inArgNames": ["z"]}'

<!-- R2 
We just say that the size is doubled and the members remain the same.
if (a,b) in z then (b,a) in v
-->
goal : (z : [int]) -> 
    {v : [int] | \(u : int), (w : int). mem (u, v) = true => mem (u , z) /\
                        len (v) == len (z) +  len (z) /\
                        ord (u, w, z) = true => 
                        (ord (u, w, v) = true /\ ord (w, u, v) = true)
                        };

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
<!-- query4 , uses zip function, reverse the list and then try zip -->
<!-- E4 -->
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'

<!-- O4, finds a solution -->
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [],
"inArgNames": ["x", "y"]}'


<!-- R4 -->
goal : (x : [a]) -> (y : [a]) -> 
{v : [pair] |  \(u : [a]), (w : a), (z : a). sndlist (v, u) = true => 
(mem (w, u) = true => mem (w, y) = true) /\ 
(ord (w, z, u) = true => ord (z, w, y))};

-----------------------------------

<!-- query5, the motivational example from the paper -->

<!-- E5  -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
 "inExamples": [{ "inputs": ["1", "2", "[49, 62, 82, 54, 76]"], 
                "output": "([49],[82,54,76])"},
                { "inputs": ["2", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49,62],[54,76])"},
                { "inputs": ["3", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49, 62, 82],[54, 76])"}],
 "inArgNames": ["x", "y", "z"]}'

<!-- O5 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
 "inExamples": [],
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




<!-- query6 Same as the summation of the list n elements query -->

<!-- E6 -->
stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [a] -> Int -> a", 
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
<!-- NthIncr -->
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[a] -> a", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "2"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'

 --by types only
 stack exec -- hplus --disable-filter=False --json='{"query": "Int -> [a] -> a", 
 "inExamples": [],
 "inArgNames": ["x", "y"]}'
--------------------------
query8
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


stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [],
"inArgNames": ["x", "y"]}'


stack exec -- hplus --disable-filter=False --json='{"query": "[Int] -> (Int, Int) -> Bool", 
 "inExamples": [{ "inputs": [ "[1,2,3]", "(2,3)"], 
                "output": "True"},
                { "inputs": [ "[1,2,3]", "(2,4)"], 
                "output": "False"}],
                "inArgNames": ["x", "y"]}'

<!-- Define Refinement -->

goal : ??

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

<!-- Refinement type -->
goal : ??

----------------------------


<!-- 17 splitStr
None of the solutions are splitStr
String -> Char -> [String] -->

stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> [String]", 
"inExamples": [],
"inArgNames": ["x", "y"]}'

<!-- Examples  -->
stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> [String]", 
"inExamples": [{ "inputs": ["\"abc\"", "\'b\'" ], 
                "output": "["\"ab\"", "\"c\""]"},
                {"inputs": ["\"abcd\"", "\'c\'"], 
                "output": "["\"abc\"", "\"d\""]"}],
"inArgNames": ["x", "y"]}'




<!-- Fails to find a solution -->
stack exec -- hplus --disable-filter=False --json='{"query": "String -> Char -> [String]", 
"inExamples": [{ "inputs": ["\"abc\"", "\'b\'" ], 
                "output": "["\"ab\"", "\"c\""]" }],
"inArgNames": ["x", "y"]}'


<!-- Refinement types -->
goal = ??



--------------------


<!-- 18 lookup
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




-----------------------------
<!-- 27 splitAtFirst
a -> [a] -> ([a], [a]) -->