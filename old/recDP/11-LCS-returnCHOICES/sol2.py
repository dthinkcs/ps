
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
# O(nm*min(n, m)) time | O((min(n, m))^2) space
4
def longestCommonSubsequence(str1, str2):
5
    small = str1 if len(str1) < len(str2) else str2
6
    big = str1 if len(str1) >= len(str2) else str2
7
    evenLcs = [[] for x in range(len(small) + 1)]
8
    oddLcs = [[] for x in range(len(small) + 1)]
9
    for i in range(1, len(big) + 1):
10
        if i % 2 == 1:
11
            currentLcs = oddLcs
12
            previousLcs = evenLcs
13
        else:
14
            currentLcs = evenLcs
15
            previousLcs = oddLcs
16
        for j in range(1, len(small) + 1):
17
            if big[i - 1] == small[j - 1]:
18
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
19
            else:
20
                currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key = len)
21
    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]
22
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
