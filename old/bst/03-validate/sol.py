
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
Validate BST
​
You are given a Binary Tree data structure consisting of Binary Tree nodes. Each Binary Tree node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value. Write a function that returns a boolean representing whether or not the Binary Tree is a valid BST. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values.
​
Sample input:
            10
          /       \
        5         15
      /    \     /      \
    2      5 13     22
  /                  \
1                    14
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(d) space
4
def validateBst(tree):
5
    return validateBstHelper(tree, float("-inf"), float("inf"))
6
​
7
def validateBstHelper(tree, minValue, maxValue):
8
    if tree is None:
9
        return True
10
    if tree.value < minValue or tree.value >= maxValue:
11
        return False
12
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
13
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
14
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be greater than or equal to some other value (the value of its closest left parent).
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
