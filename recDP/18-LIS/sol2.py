
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
Longest Increasing Subsequence
​
Given a non-empty array of integers, write a function that returns the longest strictly-increasing subsequence of the array. A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array. Assume that there will only be one longest increasing subsequence.
​
Sample input: [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
Sample output: [-24, 2, 3, 5, 6, 35]
​
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
# O(nlogn) time | O(n) space
4
def longestIncreasingSubsequence(array):
5
    sequences = [None for x in array]
6
    indices = [None for x in range(len(array) + 1)]
7
    length = 0
8
    for i, num in enumerate(array):
9
        newLength = binarySearch(1, length, indices, array, num)
10
        sequences[i] = indices[newLength - 1]
11
        indices[newLength] = i
12
        length = max(length, newLength)
13
    return buildSequence(array, sequences, indices[length])
14
​
15
def binarySearch(startIdx, endIdx, indices, array, num):
16
    if startIdx > endIdx:
17
        return startIdx
18
    middleIdx = (startIdx + endIdx) // 2
19
    if array[indices[middleIdx]] < num:
20
        startIdx = middleIdx + 1
21
    else:
22
        endIdx = middleIdx - 1
23
    return binarySearch(startIdx, endIdx, indices, array, num)
24
​
25
def buildSequence(array, sequences, currentIdx):
26
    sequence = []
27
    while currentIdx is not None:
28
        sequence.append(array[currentIdx])
29
        currentIdx = sequences[currentIdx]
30
    return list(reversed(sequence))
31
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building an array of the same length as the input array. At each index in this new array, store the length of the longest increasing subsequence ending with the number found at that index in the input array.
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
        self.assertEqual(program.longestIncreasingSubsequence([-1]), [-1])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.longestIncreasingSubsequence([-1, 2]), [-1, 2])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.longestIncreasingSubsequence([-1, 2, 1, 2]), [-1, 1, 2])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.longestIncreasingSubsequence([1, 5, -1, 10]), [1, 5, 10])
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
