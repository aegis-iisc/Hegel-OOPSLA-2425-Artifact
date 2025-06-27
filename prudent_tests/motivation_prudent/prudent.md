Failing Queries
Query1
- x:Int -> y:Int -> z:[a] -> [a]
 0
 2
[1,3,5,6]
[1,3,5,6,1,5]

1
2
[1,3,5,6]
[1,3,5,6,3,5]


0
2
['a','b','c','d']
['a','b','c','d', 'a','c']
Possible outputs: 
reverse (z!!y : (z!!x : (reverse z)))

append ( z, 

cons ((z!!x),  singleton (z!!y))
)


*********************************************************
Query2
Reverse and append the list
- x : [a] -> [a]
[1,2]
[1,2,2,1]

[1,2,3,4]
[1,2,3,4,4,3,2,1]

['a','b']
['a','b','b','a']


Required output: x ++ reverse (x)
**************************************************************
Query3
-Num a => x:[a] -> y:Int -> a
-find the sum of first y elements of x-
[49, 62, 82, 54, 76]
2
111

[49, 62, 82, 54, 76]
3
193

[1,3,5]
2
4

Finds a solution: \x y. sum (take y x)

--change the query a bit and ask for the sum of last y elements of x--
[49, 62, 82, 54, 76]
2
130

[49, 62, 82, 54, 76]
3
212

[49, 62, 82, 54, 76]
1
76

[49, 62, 82, 54, 76]
4
274

[49, 62, 82, 54, 76]
5
323

Fails to find a solution even after a very detailed list of examples 
Required output: \x y. sum (take y (reverse x))

*********************************************************************
Query 4
- x:[a] -> y:[b] -> [(a, b)]

[1,2]
[3,4]
[(1,3), (2,4)]

['a','b']
['c','d']
[('a','c'),('b','d')]

Finds a solution: \x y. zip x y 

But if we refine the query to first reverse the second list (or the first list) then times out.

[1,2]
[3,4]
[(1,4), (2,3)]

['a','b']
['c','d']
[('a','d'),('b','c')]

No solution: Required output: \x y. zip x (reverse y)
*********************************************************
Query 5, the motivational example from the paper.


- An Example without reverse function, taken from the Hoogle+ paper 
x:Int -> y:Int -> z:[a] -> ([a], [a])

Solution(s) found: without any example : 
	\x y z -> splitAt x (drop y z)
	\x y z -> splitAt y (drop x z)
\x y z -> splitAt x (take y z)
\x y z -> splitAt y (take x z)
\x y z -> splitAt x (tail (drop y z))
...










-- Refine it to deconstruct the pair and take x element from the first projection
- Required Solution: ((take x (fst (splitAt y z))), snd (splitAt y z))

1
2
[49, 62, 82, 54, 76]
([49],[82,54,76])

2
3
[49, 62, 82, 54, 76]
([49,62],[54,76])

3
3
[49, 62, 82, 54, 76]
([49, 62, 82],[54, 76])


0
2
[49, 62, 82, 54, 76]
([],[82,54, 76])


-- Or even for a much simpler solution

2
4
[49, 62, 82, 54, 76]
([54,82],[62,49])


\x y z -> splitAt x (reverse (take y z))

