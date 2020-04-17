
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
BST Construction
​
Write a Binary Search Tree (BST) class. The class should have a "value" property set to be an integer, as well as "left" and "right" properties, both of which should point to either the None (null) value or to another BST. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. The BST class should support insertion, searching, and removal of values. The removal method should only remove the first instance of the target value.
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
Solution #1Solution #2
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class BST:
4
    def __init__(self, value):
5
        self.value = value
6
        self.left = None
7
        self.right = None
8
​
9
    # Average: O(log(n)) time | O(log(n)) space
10
    # Worst: O(n) time | O(n) space
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
20
            else:
21
                self.right.insert(value)
22
        return self
23
​
24
    # Average: O(log(n)) time | O(log(n)) space
25
    # Worst: O(n) time | O(n) space
26
    def contains(self, value):
27
        if value < self.value:
28
            if self.left is None:
29
                return False
30
            else:
31
                return self.left.contains(value)
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
As you try to insert, find, or a remove a value into, in, or from a BST, you will have to traverse the tree's nodes. The BST property allows you to eliminate half of the remaining tree at each node that you traverse: if the target value is strictly smaller than a node's value, then it must be (or can only be) located to the left of the node, otherwise it must be (or can only be) to the right of that node.
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
test1 = program.BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
6
​
7
test2 = program.BST(10).insert(15).insert(11).insert(22).remove(10)
8
​
9
test3 = program.BST(10).insert(5).insert(7).insert(2).remove(10)
10
​
11
test4 = program.BST(10).insert(5).insert(15).insert(22).insert(17).insert(34) \
12
.insert(7).insert(2).insert(5).insert(1).insert(35).insert(27).insert(16) \
13
.insert(30).remove(22).remove(17)
14
​
15
def inOrderTraverse(tree, array):
16
    if tree is not None:
17
        inOrderTraverse(tree.left, array)
18
        array.append(tree.value)
19
        inOrderTraverse(tree.right, array)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
