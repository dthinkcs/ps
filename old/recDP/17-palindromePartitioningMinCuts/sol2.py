
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
Palindrome Partitioning Min Cuts
​
Given a non-empty string, write a function that returns the minimum number of cuts needed to perform on the string such that each remaining substring is a palindrome. A palindrome is defined as a string that is written the same forward as backward. Note that single-character strings are palindromes.
​
Sample input: "noonabbad"
Sample output: 2 ("noon | abba | d")
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
# O(n^2) time | O(n^2) space
4
def palindromePartitioningMinCuts(string):
5
    palindromes = [[False for i in string] for j in string]
6
    for i in range(len(string)):
7
        palindromes[i][i] = True
8
    for length in range(2, len(string) + 1):
9
        for i in range(0, len(string) - length + 1):
10
            j = i + length - 1
11
            if length == 2:
12
                palindromes[i][j] = string[i] == string[j]
13
            else:
14
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]
15
    cuts = [float("inf") for i in string]
16
    for i in range(len(string)):
17
        if palindromes[0][i]:
18
            cuts[i] = 0
19
        else:
20
            cuts[i] = cuts[i - 1] + 1
21
            for j in range(1, i):
22
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
23
                    cuts[i] = cuts[j - 1] + 1
24
    return cuts[-1]
25
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try building a two-dimensional array of the palindromicities of all substrings of the input string. Let the value stored at row i and at column j represent the palindromicity of the substring starting at index i and ending at index j.
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
        self.assertEqual(program.palindromePartitioningMinCuts("a"), 0)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.palindromePartitioningMinCuts("abba"), 0)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.palindromePartitioningMinCuts("abbba"), 0)
15

16
    def test_case_4(self):
17
        self.assertEqual(program.palindromePartitioningMinCuts("abb"), 1)
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
