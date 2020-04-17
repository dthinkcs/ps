
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
Min Number Of Coins For Change
​
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.
​
Sample input: 7, [1, 5, 10]
Sample output: 3 (2x1 + 1x5)
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
def minNumberOfCoinsForChange(n, denoms):
5
    numOfCoins = [float("inf") for amount in range(n + 1)]
6
    numOfCoins[0] = 0
7
    for denom in denoms:
8
        for amount in range(len(numOfCoins)):
9
            if denom <= amount:
10
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
11
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
12
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Try building an array of the minimum number of coins needed to make change for all amounts between 0 and n inclusive. Note that no coins are needed to make change for 0: in order to make change for 0, you do not need to use any coins.
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
        self.assertEqual(program.minNumberOfCoinsForChange(0, [1, 2, 3]), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.minNumberOfCoinsForChange(3, [2, 1]), 2)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.minNumberOfCoinsForChange(4, [1, 5, 10]), 4)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.minNumberOfCoinsForChange(7, [1, 5, 10]), 3)
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
