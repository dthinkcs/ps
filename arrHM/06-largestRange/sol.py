
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
Largest Range
​
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.
​
Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample output: [0, 7]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
1
def largestRange(arr):
2
    # Write your code here.
3
    visited = dict()
4
    for num in arr:
5
        visited[num] = False
6

7
    ranges = [0, 0]
8
    maxRanges = [0, 0]
9
    for num in arr:
10
        if not visited[num]:
11
            temp = num
12
            visited[num] = True
13
            while True:
14
                if num + 1 not in arr:
15
                    ranges[1] = num
16
                    break
17
                else:
18
                    visited[num + 1] = True
19
                num += 1
20

21

22
            while True:
23
                if temp - 1 not in arr:
24
                    ranges[0] = temp
25
                    break
26
                else:
27
                    visited[temp - 1] = True
28
                temp -= 1
29

30
        if (ranges[1] - ranges[0]) >= (maxRanges[1] - maxRanges[0]):
31
            maxRanges = ranges[:]
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
How can you use a hash table to solve this problem with an algorithm that runs in linear time?
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
​
7
    def test_case_1(self):
8
        self.assertEqual(program.largestRange([1]), [1, 1])
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.largestRange([1, 2]), [1, 2])
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.largestRange([4, 2, 1, 3]), [1, 4])
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.largestRange([4, 2, 1, 3, 6]), [1, 4])
18
​
19
    def test_case_5(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
