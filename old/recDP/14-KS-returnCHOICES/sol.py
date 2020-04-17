
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
Knapsack Problem
​
You are given an array of arrays. Each subarray in this array holds two integer values and represents an item; the first integer is the item's value, and the second integer is the item's weight. You are also given an integer representing the maximum capacity of a knapsack that you have. Your goal is to fit items in your knapsack, all the while maximizing their combined value. Note that the sum of the weights of the items that you pick cannot exceed the knapsack's capacity. Write a function that returns the maximized combined value of the items that you should pick, as well as an array of the indices of each item picked. Assume that there will only be one combination of items that maximizes the total value in the knapsack.
​
Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
Sample output: [10, [1, 3]]
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
# O(nc) time | O(nc) space
4
def knapsackProblem(items, capacity):
5
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
6
    for i in range(1, len(items) + 1):
7
        currentWeight = items[i - 1][1]
8
        currentValue = items[i - 1][0]
9
        for c in range(0, capacity + 1):
10
            if currentWeight > c:
11
                knapsackValues[i][c] = knapsackValues[i - 1][c]
12
            else:
13
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
14
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]
15
​
16
def getKnapsackItems(knapsackValues, items):
17
    sequence = []
18
    i = len(knapsackValues) - 1
19
    c = len(knapsackValues[0]) - 1
20
    while i > 0:
21
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
22
            i -= 1
23
        else:
24
            sequence.append(i - 1)
25
            c -= items[i - 1][1]
26
            i -= 1
27
        if c == 0:
28
            break
29
    return list(reversed(sequence))
30
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building a two-dimensional array of the maximum values that knapsacks of all capacities between 0 and c inclusive could hold, given one, two, three, etc., items. Let columns represent capacities and rows represent items.
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
        self.assertEqual(program.knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.knapsackProblem([[465, 100], [400, 85], [255, 55], [350, 45], [650, 130], [1000, 190], [455, 100], [100, 25], [1200, 190], [320, 65], [750, 100], [50, 45], [550, 65], [100, 50], [600, 70], [240, 40]], 200), [1500, [3, 12, 14]])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.knapsackProblem([[465, 100], [400, 85], [255, 55], [350, 45], [650, 130], [1000, 190], [455, 100], [100, 25], [1200, 190], [320, 65], [750, 100], [50, 45], [550, 65], [100, 50], [600, 70], [255, 40]], 200), [1505, [7, 12, 14, 15]])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.knapsackProblem([[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]], 100), [101, [0, 2, 3]])
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
