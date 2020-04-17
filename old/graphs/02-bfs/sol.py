
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
Breadth-first Search
​
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a simple tree-like structure. Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the Nodes' names in the input array, and returns it.
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
        self.name = name
6
        self.children = []
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
    def breadthFirstSearch(self, array):
14
        queue = [self]
15
        while len(queue) > 0:
16
            current = queue.pop(0)
17
            array.append(current.name)
18
            for child in current.children:
19
                queue.append(child)
20
        return array
21
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
The Breadth-first Search algorithm works by traversing a graph level by level. In other words, before traversing any Node's children Nodes, its sibling nodes must be traversed. How can you simply and effectively keep track of Nodes' children Nodes as you traverse them, all the while retaining the order in which you must traverse them?
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
