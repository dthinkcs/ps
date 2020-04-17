
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
Water Area
​
You are given an array of integers. Each non-zero integer represents the height of a pillar of width 1. Imagine water being poured over all of the pillars and return the surface area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored. Refer to the first minute of the video explanation below for a visual example.
​
Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
Sample output: 48
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
# O(n) time | O(n) space
4
def waterArea(heights):
5
    maxes = [0 for x in heights]
6
    leftMax = 0
7
    for i in range(len(heights)):
8
        height = heights[i]
9
        maxes[i] = leftMax
10
        leftMax = max(leftMax, height)
11
    rightMax = 0
12
    for i in reversed(range(len(heights))):
13
        height = heights[i]
14
        minHeight = min(rightMax, maxes[i])
15
        if height < minHeight:
16
            maxes[i] = minHeight - height
17
        else:
18
            maxes[i] = 0
19
        rightMax = max(rightMax, height)
20
    return sum(maxes)
21
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
In order to calculate the amount of water above a single point in the input array, you must know the height of the tallest pillar to its left and the height of the tallest pillar to its right.
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
        self.assertEqual(program.waterArea([]), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.waterArea([0, 0, 0, 0, 0]), 0)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.waterArea([0, 1, 0, 0, 0]), 0)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.waterArea([0, 1, 1, 0, 0]), 0)
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
