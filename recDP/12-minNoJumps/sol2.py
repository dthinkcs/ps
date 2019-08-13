
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
Min Number Of Jumps
​
You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward. For example, if the element at index 1 is 3, you can go from index 1 to index 2, 3, or 4. Write a function that returns the minimum number of jumps needed to reach the final index. Note that jumping from index i to index i + x always constitutes 1 jump, no matter how large x is.
​
Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
Sample output: 4 (3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)
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
def minNumberOfJumps(array):
5
    if len(array) == 1:
6
        return 0
7
    jumps = 0
8
    maxReach = array[0]
9
    steps = array[0]
10
    for i in range(1, len(array) - 1):
11
        maxReach = max(maxReach, i + array[i])
12
        steps -= 1
13
        if steps == 0:
14
            jumps += 1
15
            steps = maxReach - i
16
    return jumps + 1
17
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building an array of the minimum number of jumps needed to go from index 0 to all indices. Start at index 0 and progressively build up the array, using previously calculated values to find next ones.
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
        self.assertEqual(program.minNumberOfJumps([1]), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.minNumberOfJumps([1, 1]), 1)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.minNumberOfJumps([3, 1]), 1)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.minNumberOfJumps([1, 1, 1]), 2)
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
