
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
Max Sum Increasing Subsequence
​
Given an non-empty array of integers, write a function that returns an array of length 2. The first element in the output array should be an integer value representing the greatest sum that can be generated from a strictly-increasing subsequence in the array. The second element should be an array of the numbers in that subsequence. A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array. Assume that there will only be one increasing subsequence with the greatest sum.
​
Sample input: [10, 70, 20, 30, 50, 11, 30]
Sample output: [110, [10, 20, 30, 50]]
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
def maxSumIncreasingSubsequence(array):
5
    sequences = [None for x in array]
6
    sums = [num for num in array]
7
    maxSumIdx = 0
8
    for i in range(len(array)):
9
        currentNum = array[i]
10
        for j in range(0, i):
11
            otherNum = array[j]
12
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
13
                sums[i] = sums[j] + currentNum
14
                sequences[i] = j
15
        if sums[i] >= sums[maxSumIdx]:
16
            maxSumIdx = i
17
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]
18
​
19
def buildSequence(array, sequences, currentIdx):
20
    sequence = []
21
    while currentIdx is not None:
22
        sequence.append(array[currentIdx])
23
        currentIdx = sequences[currentIdx]
24
    return list(reversed(sequence))
25
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Try building an array of the same length as the input array. At each index in this new array, store the maximum sum that can be generated from an increasing subsequence ending with the number found at that index in the input array.
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
        self.assertEqual(program.maxSumIncreasingSubsequence([1]), [1, [1]])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.maxSumIncreasingSubsequence([-1]), [-1, [-1]])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.maxSumIncreasingSubsequence([-1, 1]), [1, [1]])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.maxSumIncreasingSubsequence([5, 4, 3, 2, 1]), [5, [5]])
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
