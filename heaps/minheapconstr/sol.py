
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
Min Heap Construction
​
Implement a Min Heap class. The class should support insertion, removal (of the minimum / root value), peeking (of the minimum / root value), as well as sifting a value up and down the heap and building the heap from an input array. The heap should be represented in the form of an array.
​
Sample input: [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
-> buildHeap(array)
-> insert(76)
-> remove()
-> remove()
-> insert(87)
Sample output:
-> [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
-> [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
-> [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class MinHeap:
4
    def __init__(self, array):
5
        self.heap = self.buildHeap(array)
6
​
7
    # O(n) time | O(1) space
8
    def buildHeap(self, array):
9
        firstParentIdx = (len(array) - 2) // 2
10
        for currentIdx in reversed(range(firstParentIdx + 1)):
11
            self.siftDown(currentIdx, len(array) - 1, array)
12
        return array
13
​
14
    # O(log(n)) time | O(1) space
15
    def siftDown(self, currentIdx, endIdx, heap):
16
        childOneIdx = currentIdx * 2 + 1
17
        while childOneIdx <= endIdx:
18
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
19
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
20
                idxToSwap = childTwoIdx
21
            else:
22
                idxToSwap = childOneIdx
23
            if heap[idxToSwap] < heap[currentIdx]:
24
                self.swap(currentIdx, idxToSwap, heap)
25
                currentIdx = idxToSwap
26
                childOneIdx = currentIdx * 2 + 1
27
            else:
28
                return
29
​
30
    # O(log(n)) time | O(1) space
31
    def siftUp(self, currentIdx, heap):
32
        parentIdx = (currentIdx - 1) // 2
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
For the buildHeap(), remove(), and insert() methods of the Heap, you will need to use the siftDown() and siftUp() methods. These two methods should essentially allow you to take any node in the heap and move it either down or up in the heap until it's in its final, appropriate position. This can be done by comparing the node in question to its child nodes in the case of siftDown() or to its parent node in the case of siftUp().
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
test1 = program.MinHeap([2, 3, 1])
6
​
7
test2 = program.MinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
8
​
9
test3 = program.MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
10
test3.insert(76)
11
test3.remove()
12
test3.remove()
13
test3.insert(87)
14
​
15
test4 = program.MinHeap([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8])
16
​
17
test5 = program.MinHeap([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])
18
test5.remove()
19
test5.insert(-8)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
