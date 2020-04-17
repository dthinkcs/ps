
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
Underscorify Substring
​
Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores. If two instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these two substrings should only appear on the far left of the left substring and on the far right of the right substring. If the main string does not contain the other string at all, return the main string intact.
​
Sample input: "testthis is a testtest to see if testestest it works", "test"
Sample output: "_test_this is a _testtest_ to see if _testestest_ it works"
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
# O(n*m) | O(n) space
4
def underscorifySubstring(string, substring):
5
    locations = collapse(getLocations(string, substring))
6
    return underscorify(string, locations)
7
​
8
def getLocations(string, substring):
9
    locations = []
10
    startIdx = 0
11
    while startIdx < len(string):
12
        nextIdx = string.find(substring, startIdx)
13
        if nextIdx != -1:
14
            locations.append([nextIdx, nextIdx + len(substring)])
15
            startIdx = nextIdx + 1
16
        else:
17
            break
18
    return locations
19
​
20
def collapse(locations):
21
    if not len(locations):
22
        return locations
23
    newLocations = [locations[0]]
24
    previous = newLocations[0]
25
    for i in range(1, len(locations)):
26
        current = locations[i]
27
        if current[0] <= previous[1]:
28
            previous[1] = current[1]
29
        else:
30
            newLocations.append(current)
31
            previous = current
32
    return newLocations
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
The first thing you need to do to solve this question is to get the locations of all instances of the substring in the main string. Try traversing the main string one character at a time and calling whatever substring-matching function is built into the language you're working in. Store a 2D array of locations, where each subarray holds the starting and ending indices of a specific instance of the substring in the main string.
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
        self.assertEqual(program.underscorifySubstring("this is a test to see if it works", "test"), "this is a _test_ to see if it works")
9

10
    def test_case_2(self):
11
        self.assertEqual(program.underscorifySubstring("test this is a test to see if it works", "test"), "_test_ this is a _test_ to see if it works")
12

13
    def test_case_3(self):
14
        self.assertEqual(program.underscorifySubstring("testthis is a test to see if it works", "test"), "_test_this is a _test_ to see if it works")
15

16
    def test_case_4(self):
17
        self.assertEqual(program.underscorifySubstring("testthis is a testest to see if testestes it works", "test"), "_test_this is a _testest_ to see if _testest_es it works")
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
