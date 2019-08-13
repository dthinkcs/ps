
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
Longest Common Subsequence
​
Implement a function that returns the longest subsequence common to two given strings. A subsequence is defined as a group of characters that appear sequentially, with no importance given to their actual position in a string. In other words, characters do not need to appear consecutively in order to form a subsequence. Assume that there will only be one longest common subsequence.
​
Sample input: "ZXVVYZW", "XKYKZPW"
Sample output: ["X", "Y", "Z", "W"]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3Solution #4
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(nm) time | O(nm) space
4
def longestCommonSubsequence(str1, str2):
5
    lengths = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
6
    for i in range(1, len(str2) + 1):
7
        for j in range(1, len(str1) + 1):
8
            if str2[i - 1] == str1[j - 1]:
9
                lengths[i][j] = lengths[i - 1][j - 1] + 1
10
            else:
11
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
12
    return buildSequence(lengths, str1)
13
​
14
def buildSequence(lengths, string):
15
    sequence = []
16
    i = len(lengths) - 1
17
    j = len(lengths[0]) - 1
18
    while i != 0 and j != 0:
19
        if lengths[i][j] == lengths[i - 1][j]:
20
            i -= 1
21
        elif lengths[i][j] == lengths[i][j - 1]:
22
            j -= 1
23
        else:
24
            sequence.append(string[j - 1])
25
            i -= 1
26
            j -= 1
27
    return list(reversed(sequence))
28
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building a two-dimensional array of the longest common subsequences of substring pairs of the input strings. Let the rows of the array represent substrings of the second input string str2. Let the first row represent the empty string. Let each row i thereafter represent the substrings of str2 from 0 to i, with i excluded. Let the columns similarly represent the first input string str1.
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
        self.assertEqual(program.longestCommonSubsequence("", ""), [])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.longestCommonSubsequence("", "ABCDEFG"), [])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.longestCommonSubsequence("ABCDEFG", ""), [])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.longestCommonSubsequence("ABCDEFG", "ABCDEFG"), ["A", "B", "C", "D", "E", "F", "G"])
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
