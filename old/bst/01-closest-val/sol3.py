
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
Find Closest Value In BST
​
You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. You are also given a target integer value; write a function that finds the closest value to that target value contained in the BST. Assume that there will only be one closest value.
​
Sample input:
            10           , 12
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
Solution #1Solution #2
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# Average: O(log(n)) time | O(log(n)) space
4
# Worst: O(n) time | O(n) space
5
def findClosestValueInBst(tree, target):
6
    return findClosestValueInBstHelper(tree, target, float("inf"))
7
​
8
def findClosestValueInBstHelper(tree, target, closest):
9
    if tree is None:
10
        return closest
11
    if abs(target - closest) > abs(target - tree.value):
12
        closest = tree.value
13
    if target < tree.value:
14
        return findClosestValueInBstHelper(tree.left, target, closest)
15
    elif target > tree.value:
16
        return findClosestValueInBstHelper(tree.right, target, closest)
17
    else:
18
        return closest
19
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try traversing the BST node by node, all the while keeping track of the node with the value closest to the target value. Calculating the absolute value of the difference between a node's value and the target value should allow you to check if that node is closer than the current closest one.
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
