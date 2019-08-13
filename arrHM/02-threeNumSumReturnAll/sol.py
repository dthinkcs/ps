
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
Three Number Sum
​
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.
​
Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
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
def threeNumberSum(array, targetSum):
5
    array.sort()
6
    triplets = []
7
    for i in range(len(array) - 2):
8
        left = i + 1
9
        right = len(array) - 1
10
        while left < right:
11
            currentSum = array[i] + array[left] + array[right]
12
            if currentSum == targetSum:
13
                triplets.append([array[i], array[left], array[right]])
14
                left += 1
15
                right -= 1
16
            elif currentSum < targetSum:
17
                left += 1
18
            elif currentSum > targetSum:
19
                right -= 1
20
    return triplets
21
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Using three for loops to calculate the sums of all possible triplets in the array would generate an algorithm that runs in O(n^3) time, where n is the length of the input array. Can you come up with something faster using only two for loops?
Output:Custom Output
Raw Output
​
Tests:Our Tests
Your Tests
Hide
Show

No changes made.
1
# Add, edit, or remove tests in this file.
2
# Treat it as your playground!
3
​
4
import program
5
import unittest
6
​
7
​
8
class TestProgram(unittest.TestCase):
9

10
    def test_case_1(self):
11
        self.assertEqual(program.threeNumberSum([1, 2, 3], 6), [[1, 2, 3]])
12

13
    def test_case_2(self):
14
        self.assertEqual(program.threeNumberSum([1, 2, 3], 7), [])
15

16
    def test_case_3(self):
17
        self.assertEqual(program.threeNumberSum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])
18

19
    def test_case_4(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
