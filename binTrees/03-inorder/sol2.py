
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

Don't forget to scroll to the bottom of the page for the video explanation!
Question:_
No changes made.


​
Iterative In-order Traversal
​
Write a function that takes in a Binary Tree and traverses it using the in-order traversal technique but without using recursion. As the tree is being traversed, a callback function passed in as an argument to the main function should be called on each node (i.e. callback(currentNode)). Each Binary Tree node has a value stored in a property called "value," a parent node in a property called "parent," and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.
​
Sample input:
            1
          /     \
        2        3
      /         /     \
    4       6        7
      \
        9
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(1) space
4
def iterativeInOrderTraversal(tree, callback):
5
    previousNode = None
6
    currentNode = tree
7
    while currentNode is not None:
8
        if previousNode is None or previousNode == currentNode.parent:
9
            if currentNode.left is not None:
10
                nextNode = currentNode.left
11
            else:
12
                callback(currentNode)
13
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
14
        elif previousNode == currentNode.left:
15
            callback(currentNode)
16
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
17
        else:
18
            nextNode = currentNode.parent
19
        previousNode = currentNode
20
        currentNode = nextNode
21
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Start by realizing that in-order traversal always traverses left child nodes before parent nodes before right child nodes. In other words, you will somehow have to traverse the entire left side of the input Binary Tree before calling the input callback on the root node and before traversing the entire right side.
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
    def __init__(self, value, parent = None):
7
        self.value = value
8
        self.left = None
9
        self.right = None
10
        self.parent = parent
11
​
12
    def insert(self, values, i = 0):
13
        if i >= len(values):
14
            return
15
        queue = [self]
16
        while len(queue) > 0:
17
            current = queue.pop(0)
18
            if current.left is None:
19
                current.left = BinaryTree(values[i], current)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
