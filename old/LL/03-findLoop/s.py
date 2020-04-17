
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
Find Loop
​
Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail node points to some node in the list instead of the None (null) value). The function should return the node (the actual node - not just its value) from which the loop originates in constant space. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property pointing to the next node in the list.
​
Sample input:
n0 -> n1 -> n2 -> n3 -> n4 -> n5 -> n6
                        ^            v
                        n9 <- n8 <- n7
Sample output: n4
​
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
def findLoop(head):
5
    first = head.next
6
    second = head.next.next
7
    while first != second:
8
        first = first.next
9
        second = second.next.next
10
    first = head
11
    while first != second:
12
        first = first.next
13
        second = second.next
14
    return first
15
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try traversing the linked list with two pointers, one iterating through every single node in the list and another iterating through every other node in the list (skipping a node every time). Eventually, both pointers will point to the same node since there is a loop in the list and since one pointer is moving faster than the other. Stop once the pointers overlap each other. How can you find the origin of the loop from here?
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
class LinkedList:
6
    def __init__(self, value):
7
        self.value = value
8
        self.next = None
9
​
10
    def addMany(self, values):
11
        current = self
12
        while current.next is not None:
13
            current = current.next
14
        for value in values:
15
            current.next = LinkedList(value)
16
            current = current.next
17
        return self
18
​
19
    def getNthNode(self, n):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
