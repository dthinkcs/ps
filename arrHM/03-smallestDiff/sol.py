
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
Smallest Difference
​
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the first array in the first position. Assume that there will only be one pair of numbers with the smallest difference.
​
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]
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
# O(nlog(n) + mlog(m)) time | O(1) space
4
def smallestDifference(arrayOne, arrayTwo):
5
    arrayOne.sort()
6
    arrayTwo.sort()
7
    idxOne = 0
8
    idxTwo = 0
9
    smallest = float("inf")
10
    current = float("inf")
11
    smallestPair = []
12
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
13
        firstNum = arrayOne[idxOne]
14
        secondNum = arrayTwo[idxTwo]
15
        if firstNum < secondNum:
16
            current = secondNum - firstNum
17
            idxOne += 1
18
        elif secondNum < firstNum:
19
            current = firstNum - secondNum
20
            idxTwo += 1
21
        else:
22
            return [firstNum, secondNum]
23
        if smallest > current:
24
            smallest = current
25
            smallestPair = [firstNum, secondNum]
26
    return smallestPair
27
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Instead of generating all possible pairs of numbers, try somehow only looking at pairs that you know could actually have the smallest difference. How can you accomplish this?
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
        self.assertEqual(program.smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]), [20, 17])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031]), [25, 1005])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.smallestDifference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]), [25, 1005])
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
