
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
BST Traversal
​
You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. Write three functions that take in an empty array, traverse the BST, add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order traversal, pre-order traversal, and post-order traversal techniques, respectively.
​
Sample input:
            10
          /       \
        5         15
      /    \            \
    2      5           22
  /
1
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(n) space
4
def inOrderTraverse(tree, array):
5
    if tree is not None:
6
        inOrderTraverse(tree.left, array)
7
        array.append(tree.value)
8
        inOrderTraverse(tree.right, array)
9
    return array
10
​
11
# O(n) time | O(n) space
12
def preOrderTraverse(tree, array):
13
    if tree is not None:
14
        array.append(tree.value)
15
        preOrderTraverse(tree.left, array)
16
        preOrderTraverse(tree.right, array)
17
    return array
18
​
19
# O(n) time | O(n) space
20
def postOrderTraverse(tree, array):
21
    if tree is not None:
22
        postOrderTraverse(tree.left, array)
23
        postOrderTraverse(tree.right, array)
24
        array.append(tree.value)
25
    return array
26
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Realize that in-order traversal simply means traversing left nodes before traversing current nodes before traversing right nodes. Try implementing this algorithm recursively by calling the inOrderTraverse method on a left node, then appending the current node's value to the input array, and then calling the inOrderTraverse method on a right node.
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
class BST:
6
    def __init__(self, value):
7
        self.value = value
8
        self.left = None
9
        self.right = None
10
​
11
    def insert(self, value):
12
        if value < self.value:
13
            if self.left is None:
14
                self.left = BST(value)
15
            else:
16
                self.left.insert(value)
17
        else:
18
            if self.right is None:
19
                self.right = BST(value)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
