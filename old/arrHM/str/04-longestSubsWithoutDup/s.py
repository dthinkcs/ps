
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
Longest Substring Without Duplication
​
Write a function that takes in a string and that returns its longest substring without duplicate characters. Assume that there will only be one longest substring without duplication.
​
Sample input: "clementisacap"
Sample output: "mentisac"
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
# O(n) time | O(min(n, a)) space
4
def longestSubstringWithoutDuplication(string):
5
    lastSeen = {}
6
    longest = [0, 1]
7
    startIdx = 0
8
    for i, char in enumerate(string):
9
        if char in lastSeen:
10
            startIdx = max(startIdx, lastSeen[char] + 1)
11
        if longest[1] - longest[0] < i + 1 - startIdx:
12
            longest = [startIdx, i + 1]
13
        lastSeen[char] = i
14
    return string[longest[0]:longest[1]]
15
​
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
Try traversing the input string and storing the last position at which you see each character in a hash table. How can this help you solve the given problem?
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
        self.assertEqual(program.longestSubstringWithoutDuplication("a"), "a")
9

10
    def test_case_2(self):
11
        self.assertEqual(program.longestSubstringWithoutDuplication("abc"), "abc")
12

13
    def test_case_3(self):
14
        self.assertEqual(program.longestSubstringWithoutDuplication("abcb"), "abc")
15

16
    def test_case_4(self):
17
        self.assertEqual(program.longestSubstringWithoutDuplication("abcdeabcdefc"), "abcdef")
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
