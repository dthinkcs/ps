
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
Number Of Possible Binary Tree Topologies
​
Write a function that takes in a non-negative integer n and that returns the number of possible Binary Tree topologies that can be created with exactly n nodes. A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2: a root node with a left node, and a root node with a right node. Node that when n is equal to 0, there is one topology that can be created: the None (null) node.
​
Sample input: 3
Sample output: 5
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# Upper Bound: O((n*(2n)!)/(n!(n+1)!)) time | O(n) space
4
def numberOfBinaryTreeTopologies(n):
5
    if n == 0:
6
        return 1
7
    numberOfTrees = 0
8
    for leftTreeSize in range(n):
9
        rightTreeSize = n - 1 - leftTreeSize
10
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
11
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
12
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
13
    return numberOfTrees
14
​
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
Every Binary Tree topology of n nodes where n is greater than 0 must have a root node and an amount of nodes on both of its sides totaling n - 1. For instance, one such topology could have a root node, n - 3 nodes in its left subtree, and 2 nodes in its right subtree. Another one could have a root node, 4 nodes in its left subtree, and n - 3 nodes in its right subtree. How many distinct Binary Tree topologies with a root node, a left subtree of x nodes, and a right subtree of n - 1 - x nodes are there?
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
        self.assertEqual(program.numberOfBinaryTreeTopologies(0), 1)
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.numberOfBinaryTreeTopologies(1), 1)
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.numberOfBinaryTreeTopologies(2), 2)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.numberOfBinaryTreeTopologies(3), 5)
18
​
19
    def test_case_5(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy





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
Number Of Possible Binary Tree Topologies
​
Write a function that takes in a non-negative integer n and that returns the number of possible Binary Tree topologies that can be created with exactly n nodes. A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2: a root node with a left node, and a root node with a right node. Node that when n is equal to 0, there is one topology that can be created: the None (null) node.
​
Sample input: 3
Sample output: 5
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n^2) time | O(n) space
4
def numberOfBinaryTreeTopologies(n, cache = {0: 1}):
5
    if n in cache:
6
        return cache[n]
7
    numberOfTrees = 0
8
    for leftTreeSize in range(n):
9
        rightTreeSize = n - 1 - leftTreeSize
10
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
11
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
12
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
13
    cache[n] = numberOfTrees
14
    return numberOfTrees
15
​
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
Every Binary Tree topology of n nodes where n is greater than 0 must have a root node and an amount of nodes on both of its sides totaling n - 1. For instance, one such topology could have a root node, n - 3 nodes in its left subtree, and 2 nodes in its right subtree. Another one could have a root node, 4 nodes in its left subtree, and n - 3 nodes in its right subtree. How many distinct Binary Tree topologies with a root node, a left subtree of x nodes, and a right subtree of n - 1 - x nodes are there?
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
        self.assertEqual(program.numberOfBinaryTreeTopologies(0), 1)
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.numberOfBinaryTreeTopologies(1), 1)
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.numberOfBinaryTreeTopologies(2), 2)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.numberOfBinaryTreeTopologies(3), 5)
18
​
19
    def test_case_5(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy




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
Number Of Possible Binary Tree Topologies
​
Write a function that takes in a non-negative integer n and that returns the number of possible Binary Tree topologies that can be created with exactly n nodes. A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only two Binary Tree topologies when n is equal to 2: a root node with a left node, and a root node with a right node. Node that when n is equal to 0, there is one topology that can be created: the None (null) node.
​
Sample input: 3
Sample output: 5
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n^2) time | O(n) space
4
def numberOfBinaryTreeTopologies(n):
5
    cache = [1]
6
    for m in range(1, n + 1):
7
        numberOfTrees = 0
8
        for leftTreeSize in range(m):
9
            rightTreeSize = m - 1 - leftTreeSize
10
            numberOfLeftTrees = cache[leftTreeSize]
11
            numberOfRightTrees = cache[rightTreeSize]
12
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
13
        cache.append(numberOfTrees)
14
    return cache[n]
15
​
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
Every Binary Tree topology of n nodes where n is greater than 0 must have a root node and an amount of nodes on both of its sides totaling n - 1. For instance, one such topology could have a root node, n - 3 nodes in its left subtree, and 2 nodes in its right subtree. Another one could have a root node, 4 nodes in its left subtree, and n - 3 nodes in its right subtree. How many distinct Binary Tree topologies with a root node, a left subtree of x nodes, and a right subtree of n - 1 - x nodes are there?
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
        self.assertEqual(program.numberOfBinaryTreeTopologies(0), 1)
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.numberOfBinaryTreeTopologies(1), 1)
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.numberOfBinaryTreeTopologies(2), 2)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.numberOfBinaryTreeTopologies(3), 5)
18
​
19
    def test_case_5(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
