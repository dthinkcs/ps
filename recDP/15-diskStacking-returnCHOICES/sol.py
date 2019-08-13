
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
Disk Stacking
​
You are given a non-empty array of arrays. Each subarray holds three integers and represents a disk. These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other disk below it. Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note that you cannot rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times. Assume that there will only be one stack with the greatest total height.
​
Sample input: [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5]]
Sample output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
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
# O(n^2) time | O(n) space
4
def diskStacking(disks):
5
    disks.sort(key = lambda disk: disk[2])
6
    heights = [disk[2] for disk in disks]
7
    sequences = [None for disk in disks]
8
    maxHeightIdx = 0
9
    for i in range(1, len(disks)):
10
        currentDisk = disks[i]
11
        for j in range(0, i):
12
            otherDisk = disks[j]
13
            if areValidDimensions(otherDisk, currentDisk):
14
                if heights[i] <= currentDisk[2] + heights[j]:
15
                    heights[i] = currentDisk[2] + heights[j]
16
                    sequences[i] = j
17
        if heights[i] >= heights[maxHeightIdx]:
18
            maxHeightIdx = i
19
    return buildSequence(disks, sequences, maxHeightIdx)
20
​
21
def areValidDimensions(o, c):
22
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]
23
​
24
def buildSequence(array, sequences, currentIdx):
25
    sequence = []
26
    while currentIdx is not None:
27
        sequence.append(array[currentIdx])
28
        currentIdx = sequences[currentIdx]
29
    return list(reversed(sequence))
30
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building an array of the same length as the array of disks. At each index i in this new array, store the height of the tallest tower that can be created with the disk located at index i at the bottom.
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
class TestProgram(unittest.TestCase):
6

7
    def test_case_1(self):
8
        self.assertEqual(program.diskStacking([[2, 1, 2]]), [[2, 1, 2]])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3]]), [[2, 1, 2], [3, 2, 3]])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]), [[2, 2, 8]])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]), [[2, 1, 2], [3, 2, 3]])
18

19
    def test_case_5(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
