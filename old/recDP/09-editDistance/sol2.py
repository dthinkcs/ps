
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
Levenshtein Distance
​
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string. There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another.
​
Sample input: "abc", "yabd"
Sample output: 2 (insert "y"; substitute "c" for "d")
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
# O(nm) time | O(min(n, m)) space
4
def levenshteinDistance(str1, str2):
5
    small = str1 if len(str1) < len(str2) else str2
6
    big = str1 if len(str1) >= len(str2) else str2
7
    evenEdits = [x for x in range(len(small) + 1)]
8
    oddEdits = [None for x in range(len(small) + 1)]
9
    for i in range(1, len(big) + 1):
10
        if i % 2 == 1:
11
            currentEdits = oddEdits
12
            previousEdits = evenEdits
13
        else:
14
            currentEdits = evenEdits
15
            previousEdits = oddEdits
16
        currentEdits[0] = i
17
        for j in range(1, len(small) + 1):
18
            if big[i - 1] == small[j - 1]:
19
                currentEdits[j] = previousEdits[j - 1]
20
            else:
21
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
22
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
23
​
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
Try building a two-dimensional array of the minimum numbers of edits for pairs of substrings of the input strings. Let the rows of the array represent substrings of the second input string str2. Let the first row represent the empty string. Let each row i thereafter represent the substrings of str2 from 0 to i, with i excluded. Let the columns similarly represent the first input string str1.
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
        self.assertEqual(program.levenshteinDistance("", ""), 0)
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.levenshteinDistance("", "abc"), 3)
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.levenshteinDistance("abc", "abc"), 0)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.levenshteinDistance("abc", "abx"), 1)
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
