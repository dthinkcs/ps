
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
Kadane's Algorithm
​
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all the numbers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers.
​
Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])
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
# O(n) time | O(1) space - where n is the length of the input array
4
def kadanesAlgorithm(array):
5
    maxEndingHere = array[0]
6
    maxSoFar = array[0]
7
    for i in range(1, len(array)):
8
        num = array[i]
9
        maxEndingHere = max(num, maxEndingHere + num)
10
        maxSoFar = max(maxSoFar, maxEndingHere)
11
    return maxSoFar
12
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
This problem seems fairly simple until you run into negative numbers, some of which are so big in absolute value that they essentially break an otherwise good subarray into two subarrays, and some of which are small enough that there exists a subarray containing them whose numbers sum to maximum sum that you're looking for. How can you determine which group a negative number belongs to?
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
        self.assertEqual(program.kadanesAlgorithm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.kadanesAlgorithm([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -1)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.kadanesAlgorithm([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]), -1)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.kadanesAlgorithm([1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]), 35)
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
