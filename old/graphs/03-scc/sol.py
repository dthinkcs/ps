
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
Single Cycle Check
​
You are given an array of integers. Each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of 2 indices forward in the array; the integer -3 represents a jump of 3 indices backward in the array. If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0. Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element is visited exactly once before landing back on the starting index.
​
Sample input: [2, 3, 1, -4, -4, 2]
Sample output: True
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
# O(n) time | O(1) space - where n is the length of the input array
4
def hasSingleCycle(array):
5
    numElementsVisited = 0
6
    currentIdx = 0
7
    while numElementsVisited < len(array):
8
        if numElementsVisited > 0 and currentIdx == 0:
9
            return False
10
        numElementsVisited += 1
11
        currentIdx = getNextIdx(currentIdx, array)
12
    return currentIdx == 0
13
​
14
def getNextIdx(currentIdx, array):
15
    jump = array[currentIdx]
16
    nextIdx = (currentIdx + jump) % len(array)
17
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
In order to check if the input array has a single cycle, you have to jump through all of the elements in the array. Could you keep a counter, jump through elements in the array, and stop once you've jumped through as many elements as are contained in the array?
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
        self.assertEqual(program.hasSingleCycle([2, 2, -1]), True)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.hasSingleCycle([2, 2, 2]), True)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.hasSingleCycle([1, 1, 1, 1, 1]), True)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.hasSingleCycle([-1, 2, 2]), True)
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
