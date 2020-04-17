
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
Depth-first Search
​
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a simple tree-like structure. Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all the of the Nodes' names in the input array, and returns it.
​
Sample input:
         A
       / | \
    B  C  D
   / \       / \
E    F  G   H
      / \    \
     I   J    K
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class Node:
4
    def __init__(self, name):
5
        self.children = []
6
        self.name = name
7
​
8
    def addChild(self, name):
9
        self.children.append(Node(name))
10
        return self
11
​
12
    # O(v + e) time | O(v) space
13
    def depthFirstSearch(self, array):
14
        array.append(self.name)
15
        for child in self.children:
16
            child.depthFirstSearch(array)
17
        return array
18
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
The Depth-first Search algorithm works by traversing a graph branch by branch. In other words, before traversing any Node's sibling Nodes, its children nodes must be traversed. How can you simply and effectively keep track of Nodes' sibling Nodes as you traverse them, all the while retaining the order in which you must traverse them?
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
test1 = program.Node("A")
6
test1.addChild("B").addChild("C")
7
test1.children[0].addChild("D")
8
​
9
test2 = program.Node("A")
10
test2.addChild("B").addChild("C").addChild("D").addChild("E")
11
test2.children[1].addChild("F")
12
​
13
test3 = program.Node("A")
14
test3.addChild("B")
15
test3.children[0].addChild("C")
16
test3.children[0].children[0].addChild("D").addChild("E")
17
test3.children[0].children[0].children[0].addChild("F")
18
​
19
test4 = program.Node("A")
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
