
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
Max Profit With K Transactions
​
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day. Write a function that returns the maximum profit that you can make buying and selling the stock, given k transactions. Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share.
​
Sample input: [5, 11, 3, 50, 60, 90], 2
Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90)
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
# O(nk) time | O(n) space
4
def maxProfitWithKTransactions(prices, k):
5
    if not len(prices):
6
        return 0
7
    evenProfits = [0 for d in prices]
8
    oddProfits = [0 for d in prices]
9
    for t in range(1, k + 1):
10
        maxThusFar = float("-inf")
11
        if t % 2 == 1:
12
            currentProfits = oddProfits
13
            previousProfits = evenProfits
14
        else:
15
            currentProfits = evenProfits
16
            previousProfits = oddProfits
17
        for d in range(1, len(prices)):
18
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
19
            currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
20
    return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]
21
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building a two-dimensional array of the maximum profits you can make on each day with zero, one, two, etc., k transactions. Let columns represent days and rows represent the number of transactions.
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
        self.assertEqual(program.maxProfitWithKTransactions([], 1), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.maxProfitWithKTransactions([1], 1), 0)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.maxProfitWithKTransactions([1, 10], 1), 9)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.maxProfitWithKTransactions([1, 10], 3), 9)
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
