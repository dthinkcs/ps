
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
Maximum Subset Sum With No Adjacent Elements
​
Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements in the array. If a sum cannot be generated, the function should return 0.
​
Sample input: [75, 105, 120, 75, 90, 135]
Sample output: 330 (75, 120, 135)
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
# O(n) time | O(1) space
4
def maxSubsetSumNoAdjacent(array):
5
    if not len(array):
6
        return 0
7
    elif len(array) == 1:
8
        return array[0]
9
    second = array[0]
10
    first = max(array[0], array[1])
11
    for i in range(2, len(array)):
12
        current = max(first, second + array[i])
13
        second = first
14
        first = current
15
    return first
16
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building an array of the same length as the input array. At each index in this new array, store the maximum sum that can be generated using no adjacent numbers located between index 0 and the current index.
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
        self.assertEqual(program.maxSubsetSumNoAdjacent([]), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.maxSubsetSumNoAdjacent([1]), 1)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.maxSubsetSumNoAdjacent([1, 2]), 2)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.maxSubsetSumNoAdjacent([1, 2, 3]), 4)
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
