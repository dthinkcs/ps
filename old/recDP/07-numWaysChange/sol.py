
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
Number Of Ways To Make Change
​
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the number of ways to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal.
​
Sample input: 6, [1, 5]
Sample output: 2 (1x1 + 1x5 and 6x1)
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
# O(nd) time | O(n) space
4
def numberOfWaysToMakeChange(n, denoms):
5
    ways = [0 for amount in range(n + 1)]
6
    ways[0] = 1
7
    for denom in denoms:
8
        for amount in range(1, n + 1):
9
            if denom <= amount:
10
                ways[amount] += ways[amount - denom]
11
    return ways[n]
12
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Try building an array of the number of ways to make change for all amounts between 0 and n inclusive. Note that there is only one way to make change for 0: that is to not use any coins.
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
        self.assertEqual(program.numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.numberOfWaysToMakeChange(9, [5]), 0)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.numberOfWaysToMakeChange(7, [2, 4]), 0)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.numberOfWaysToMakeChange(6, [1, 5]), 2)
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
