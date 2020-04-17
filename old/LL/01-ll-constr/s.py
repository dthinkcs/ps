
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
Linked List Construction
​
Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, both of which should point to either the None (null) value or to a Linked List node. Every node will have a "value" property as well as "next" and "prev" properties, both of which can point to either the None (null) value or another node. The class should support setting the head and tail of the linked list, inserting nodes before and after other nodes as well as at certain positions, removing given nodes and removing nodes with specific values, and searching for nodes with values. Only the searching method should return a value: specifically, a boolean.
​
Sample input:
1 -> 2 -> 3 -> 4 -> 5
Sample output (after setting 4 to head):
4 -> 1 -> 2 -> 3 -> 5
Sample output (after setting 6 to tail):
4 -> 1 -> 2 -> 3 -> 5 -> 6
Sample output (after inserting 3 before 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class DoublyLinkedList:
4
    def __init__(self):
5
        self.head = None
6
        self.tail = None
7
​
8
    # O(1) time | O(1) space
9
    def setHead(self, node):
10
      if self.head is None:
11
        self.head = node
12
        self.tail = node
13
        return
14
      self.insertBefore(self.head, node)
15
​
16
    # O(1) time | O(1) space
17
    def setTail(self, node):
18
      if self.tail is None:
19
        self.setHead(node)
20
        return
21
      self.insertAfter(self.tail, node)
22
​
23
    # O(1) time | O(1) space
24
    def insertBefore(self, node, nodeToInsert):
25
      if nodeToInsert == self.head and nodeToInsert == self.tail:
26
        return
27
      self.remove(nodeToInsert)
28
      nodeToInsert.prev = node.prev
29
      nodeToInsert.next = node
30
      if node.prev is None:
31
        self.head = nodeToInsert
32
      else:
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
When dealing with linked lists, it's very important to keep track of pointers on nodes (i.e., the "next" and "prev" properties on the nodes). For instance, if you're inserting a node in a linked list, but that node is already located somewhere else in the linked list (in other words, if you're moving a node), it's crucial to completely update the pointers of the adjacent nodes of the node being moved before updating the node's own pointers. The order in which you update nodes' pointers will make or break your algorithm.
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
class Node:
6
  def __init__(self, value):
7
    self.value = value
8
    self.prev = None
9
    self.next = None
10
​
11
def expectEmpty(self, linkedList):
12
  self.assertEqual(linkedList.head, None)
13
  self.assertEqual(linkedList.tail, None)
14
​
15
def expectHeadTail(self, linkedList, head, tail):
16
  self.assertEqual(linkedList.head, head)
17
  self.assertEqual(linkedList.tail, tail)
18
​
19
def expectSingleNode(self, linkedList, node):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
