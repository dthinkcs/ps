
Don't show this again.

Questions List
C++
Go
Java
Javascript
Python



Theme:
algoexpert
algoexpert
blackboard
cobalt
lucario
midnight
night
oceanic-next
rubyblue
white
Keymaps:
default
default
emacs
vim

00:00

×Don't forget to scroll to the bottom of the page for the video explanation!
Question:_
No changes made.


​
River Sizes
​
You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order.
​
Sample input:
[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(wh) time | O(wh) space
4
def riverSizes(matrix):
5
    sizes = []
6
    visited = [[False for value in row] for row in matrix]
7
    for i in range(len(matrix)):
8
        for j in range(len(matrix[i])):
9
            if visited[i][j]:
10
                continue
11
            traverseNode(i, j, matrix, visited, sizes)
12
    return sizes
13
​
14
def traverseNode(i, j, matrix, visited, sizes):
15
    currentRiverSize = 0
16
    nodesToExplore = [[i, j]]
17
    while len(nodesToExplore):
18
        currentNode = nodesToExplore.pop()
19
        i = currentNode[0]
20
        j = currentNode[1]
21
        if visited[i][j]:
22
            continue
23
        visited[i][j] = True
24
        if matrix[i][j] == 0:
25
            continue
26
        currentRiverSize += 1
27
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
28
        for neighbor in unvisitedNeighbors:
29
            nodesToExplore.append(neighbor)
30
    if currentRiverSize > 0:
31
        sizes.append(currentRiverSize)
32
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Since you must return the sizes of rivers, which consist of horizontally and vertically adjacent 1s in the input matrix, you must somehow keep track of groups of neighboring 1s as you traverse the matrix. Try treating the matrix as a graph, where each element in the matrix is a node in the graph with up to 4 neighboring nodes (above, below, to the left, and to the right), and traverse it using a popular graph-traversal algorithm like Depth-first Search or Breadth-first Search.
Output:Custom Output
Raw Output
Run your code when you feel ready.
​
Tests:Our Tests
Your Tests
Hide
Show

No changes made.
1
import program
2
import unittest
3
​
4
​
5
class TestProgram(unittest.TestCase):
6
​
7
    def test_case_1(self):
8
        testInput = [[0]]
9
        expected = []
10
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)
11
​
12
    def test_case_2(self):
13
        testInput = [[1]]
14
        expected = [1]
15
        self.assertEqual(sorted(program.riverSizes(testInput)), expected)
16
​
17
    def test_case_3(self):
18
        testInput = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
19
        expected = [1, 2, 3]
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
