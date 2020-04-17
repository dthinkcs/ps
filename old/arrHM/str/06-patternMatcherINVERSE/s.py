
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
Pattern Matcher
​
You are given two non-empty strings. The first one is a pattern consisting of only "x"s and / or "y"s; the other one is a normal string of alphanumeric characters. Write a function that checks whether or not the normal string matches the pattern. A string S0 is said to match a pattern if replacing all "x"s in the pattern with some string S1 and replacing all "y"s in the pattern with some string S2 yields the same string S0. If the input string does not match the input pattern, return an empty array; otherwise, return an array holding the representations of "x" and "y" in the normal string, in that order. If the pattern does not contain any "x"s or "y"s, the respective letter should be represented by an empty string in the final array that you return. Assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y" in the input string.
​
Sample input: "xxyxxy", "gogopowerrangergogopowerranger"
Sample output: ["go", "powerranger"]
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
# O(n^2 + m) time | O(n + m) space
4
def patternMatcher(pattern, string):
5
    if len(pattern) > len(string):
6
        return []
7
    newPattern = getNewPattern(pattern)
8
    didSwitch = newPattern[0] != pattern[0]
9
    counts = {"x": 0, "y": 0}
10
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
11
    if counts["y"] != 0:
12
        for lenOfX in range(1, len(string)):
13
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
14
            if lenOfY <= 0 or lenOfY % 1 != 0:
15
                continue
16
            lenOfY = int(lenOfY)
17
            yIdx = firstYPos * lenOfX
18
            x = string[:lenOfX]
19
            y = string[yIdx:yIdx + lenOfY]
20
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
21
            if string == "".join(potentialMatch):
22
                return [x, y] if not didSwitch else [y, x]
23
    else:
24
        lenOfX = len(string) / counts["x"]
25
        if lenOfX % 1 == 0:
26
            lenOfX = int(lenOfX)
27
            x = string[:lenOfX]
28
            potentialMatch = map(lambda char: x, newPattern)
29
            if string == "".join(potentialMatch):
30
                return [x, ""] if not didSwitch else ["", x]
31
    return []
32
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Start by checking if the pattern starts with an "x". If it doesn't, consider generating a new pattern that swaps all "x"s for "y"s and vice-versa; this might greatly simplify the rest of your algorithm. Make sure to keep track of whether or not you do this swap, as your final answer will be affected by it.
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
        self.assertEqual(program.patternMatcher("xyxy", "abab"), ["a", "b"])
9

10
    def test_case_2(self):
11
        self.assertEqual(program.patternMatcher("yxyx", "abab"), ["b", "a"])
12

13
    def test_case_3(self):
14
        self.assertEqual(program.patternMatcher("yxx", "yomama"), ["ma", "yo"])
15

16
    def test_case_4(self):
17
        self.assertEqual(program.patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])
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
