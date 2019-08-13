
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
Knuth—Morris—Pratt Algorithm
​
Write a function that takes in two strings and checks if the first string contains the second one using the Knuth—Morris—Pratt algorithm. The function should return a boolean.
​
Sample input: "aefoaefcdaefcdaed", "aefcdaed"
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
# O(n + m) time | O(m) space
4
def knuthMorrisPrattAlgorithm(string, substring):
5
    pattern = buildPattern(substring)
6
    return doesMatch(string, substring, pattern)
7
​
8
def buildPattern(substring):
9
    pattern = [-1 for i in substring]
10
    j = 0
11
    i = 1
12
    while i < len(substring):
13
        if substring[i] == substring[j]:
14
            pattern[i] = j
15
            i += 1
16
            j += 1
17
        elif j > 0:
18
            j = pattern[j - 1] + 1
19
        else:
20
            i += 1
21
    return pattern
22
​
23
def doesMatch(string, substring, pattern):
24
    i = 0
25
    j = 0
26
    while i + len(substring) - j <= len(string):
27
        if string[i] == substring[j]:
28
            if j == len(substring) - 1:
29
                return True
30
            i += 1
31
            j += 1
32
        elif j > 0:
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
The Knuth—Morris—Pratt algorithm works by identifying patterns in the potential substring and exploiting them to avoid doing needless character comparisons when searching for the substring in the main string. For instance, take the string "ababac" and the substring "abac"; comparing these strings will fail at the fourth character, where "b" is not equal to "c". Instead of having to restart our comparisons at the second character of the main string, however, we notice that the substring "ab", which is at the beginning of our potential substring, just appeared near our point of failure in the main string. How can we use this to our advantage?
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
        self.assertEqual(program.knuthMorrisPrattAlgorithm("testwafwafawfawfawfawfawfawfawfa", "fawfawfawfawfa"), True)
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.knuthMorrisPrattAlgorithm("tesseatesgawatewtesaffawgfawtteafawtesftawfawfawfwfawftest", "test"), True)
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.knuthMorrisPrattAlgorithm("aaabaabacdedfaabaabaaa", "aabaabaaa"), True)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.knuthMorrisPrattAlgorithm("abxabcabcaby", "abcaby"), True)
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
