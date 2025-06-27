query1.

--by both examples and types
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [{ "inputs": ["0", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,1,5]"},
                { "inputs": ["1", "2", "[1,3,5,6]"], 
                "output": "[1,3,5,6,3,5]"},
                { "inputs": ["0", "2", "[\"abcd\"]"], 
                "output": "[\"abcdac\"]"}],
 "inArgNames": ["x", "y", "z"]}'

 --by types only
 stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [],
 "inArgNames": ["x", "y", "z"]}'


query2
stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [a]", 
 "inExamples": [{ "inputs": ["[1,2,3,4]"], 
                "output": "[1,2,3,4,4,3,2,1]"},
                { "inputs": ["[1,3,5,6]"], 
                "output": "[1,3,5,6,6,5,3,1]"},
                { "inputs": ["[\"abcd\"]"], 
                "output": "[\"abcddcba\"]"}],
 "inArgNames": ["z"]}'



query3
stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [a] -> Int -> a", 
 "inExamples": [{ "inputs": ["[49,62,82,54,76]", "2"], 
                "output": "111"},
                { "inputs": ["[49,62,82,54,76]",3], 
                "output": "193"},
                { "inputs": ["[1,3,5]",2], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'


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


 query4 

stack exec -- hplus --disable-filter=False --json='{"query": "[a] -> [b] -> [(a, b)]", 
 "inExamples": [{ "inputs": ["[1,2]", "[3,4]"], 
                "output": "[(1,4), (2,3)]"}],
                "inArgNames": ["x", "y"]}'



query5
stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> ([a], [a])", 
 "inExamples": [{ "inputs": ["1", "2", "[49, 62, 82, 54, 76]"], 
                "output": "([49],[82,54,76])"},
                { "inputs": ["2", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49,62],[54,76])"},
                { "inputs": ["3", "3", "[49, 62, 82, 54, 76]"], 
                "output": "([49, 62, 82],[54, 76])"}],
 "inArgNames": ["x", "y", "z"]}'


query6 
stack exec -- hplus --disable-filter=False --json='{"query": "Num a => [a] -> Int -> a", 
 "inExamples": [{ "inputs": ["[49,62,82,54,76]", "2"], 
                "output": "111"},
                { "inputs": ["[49,62,82,54,76]","3"], 
                "output": "193"},
                { "inputs": ["[1,3,5]","2"], 
                "output": "4"}],
 "inArgNames": ["x", "y"]}'


query7
stack exec -- hplus --disable-filter=False --json='{"query": "Int ->[a] -> a", 
 "inExamples": [{ "inputs": ["0", "[1,3,5,6]"], 
                "output": "1"},
                { "inputs": ["1", "[1,3,5,6]"], 
                "output": "3"},
                { "inputs": ["3", "[\"abcd\"]"], 
                "output": "\"c\""}],
 "inArgNames": ["x", "y"]}'

 --by types only
 stack exec -- hplus --disable-filter=False --json='{"query": "Int -> Int -> [a] -> [a]", 
 "inExamples": [],
 "inArgNames": ["x", "y", "z"]}'

query7
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



query8 rev
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
