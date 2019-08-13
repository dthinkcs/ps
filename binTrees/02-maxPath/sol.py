
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
Max Path Sum In Binary Tree
​
Write a function that takes in a Binary Tree and returns its max path sum. A path is a collection of connected nodes where no node is connected to more than two other nodes; a path sum is the sum of the values of the nodes in a particular path. Each Binary Tree node has a value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.
​
Sample input:
            1
          /     \
        2        3
      /    \    /     \
    4      5 6       7

Sample output: 18
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(log(n)) space
4
def maxPathSum(tree):
5
    _, maxSum = findMaxSum(tree)
6
    return maxSum
7
​
8
def findMaxSum(tree):
9
    if tree is None:
10
        return (0, 0)
11
​
12
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
13
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
14
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
15
​
16
    value = tree.value
17
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
18
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
19
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
20
​
21
    return (maxSumAsBranch, maxPathSum)
22
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
If you were to imagine each node in a Binary Tree as the root of the Binary Tree, temporarily eliminating all of the nodes that come above it, how would you find the max path sum for each of these newly imagined Binary Trees? In simpler terms, how can you find the max path sum for each subtree in the Binary Tree?
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
        test = BinaryTree(1).insert([2, 3])
9
        self.assertEqual(program.maxPathSum(test), 6)
10
​
11
    def test_case_2(self):
12
        test = BinaryTree(1).insert([2, -1])
13
        self.assertEqual(program.maxPathSum(test), 3)
14
​
15
    def test_case_3(self):
16
        test = BinaryTree(1).insert([-5, 3, 6])
17
        self.assertEqual(program.maxPathSum(test), 6)
18
​
19
    def test_case_4(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
