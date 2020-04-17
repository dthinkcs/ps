
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
Remove Kth Node From End
​
Write a function that takes in the head of a Singly Linked List and an integer k (assume that the list has at least k nodes). The function should remove the kth node from the end of the list. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.
​
Sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4
Sample output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
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
def removeKthNodeFromEnd(head, k):
5
    counter = 1
6
    first = head
7
    second = head
8
    while counter <= k:
9
        second = second.next
10
        counter += 1
11
    if second is None:
12
        head.value = head.next.value
13
        head.next = head.next.next
14
        return
15
    while second.next is not None:
16
        second = second.next
17
        first = first.next
18
    first.next = first.next.next
19
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Since you are given a Singly Linked List, you do not have access to any of the list's nodes' previous nodes. Thus, traversing the entire list and then counting k nodes back isn't an option. Is there a way for you to traverse the entire list and to know which node is the kth node from the end by the time you reach the final node in the list?
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
    def getNodesInArray(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
