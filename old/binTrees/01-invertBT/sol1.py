
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
Invert Binary Tree
​
Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding (mirrored) right node. Each Binary Tree node has a value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.
​
Sample input:
            1
          /     \
        2        3
      /    \    /    \
    4      5 6      7
  /   \
8      9
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
# O(n) time | O(n) space
4
def invertBinaryTree(tree):
5
    queue = [tree]
6
    while len(queue):
7
        current = queue.pop(0)
8
        if current is None:
9
            continue
10
        swapLeftAndRight(current)
11
        queue.append(current.left)
12
        queue.append(current.right)
13
​
14
def swapLeftAndRight(tree):
15
    tree.left, tree.right = tree.right, tree.left
16
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Start by inverting the root node of the Binary Tree. Inverting this root node simply consists of swapping its left and right child nodes, which can be done the same way as swapping two variables.
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
class BinaryTree:
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
    def __eq__(self, other):
12
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__
13
​
14
    def insert(self, values, i = 0):
15
        if i >= len(values):
16
            return
17
        queue = [self]
18
        while len(queue) > 0:
19
            current = queue.pop(0)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
