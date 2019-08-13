
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
Lowest Common Manager
​
You're given three inputs, all of which are instances of a class that have a "directReports" property pointing to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that is not anybody else's direct report), and the other two inputs are reports in the organizational chart. Write a function that returns the lowest common manager to the two reports.
​
Sample input: Node A, Node E, Node I (from the organizational chart below)
            A
          /     \
        B        C
      /    \    /    \
    D     E F      G
  /   \
H      I
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(d) space - where n is the number of people
4
# in the org and d is the depth (height) of the org chart
5
def getLowestCommonManager(topManager, reportOne, reportTwo):
6
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager
7
​
8
def getOrgInfo(manager, reportOne, reportTwo):
9
    numImportantReports = 0
10
    for directReport in manager.directReports:
11
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
12
        if orgInfo.lowestCommonManager is not None:
13
            return orgInfo
14
        numImportantReports += orgInfo.numImportantReports
15
    if manager == reportOne or manager == reportTwo:
16
        numImportantReports += 1
17
    lowestCommonManager = manager if numImportantReports == 2 else None
18
    return OrgInfo(lowestCommonManager, numImportantReports)
19
​
20
class OrgInfo:
21
    def __init__(self, lowestCommonManager, numImportantReports):
22
        self.lowestCommonManager = lowestCommonManager
23
        self.numImportantReports = numImportantReports
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Given a random subtree in the organizational chart, the manager at the root of that subtree is common to any two reports in the subtree.
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
class OrgChart:
6
    def __init__(self, name):
7
        self.name = name
8
        self.directReports = []
9
​
10
    def addDirectReports(self, directReports):
11
        for directReport in directReports:
12
            self.directReports.append(directReport)
13
​
14
orgCharts = {}
15
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
16
for letter in ALPHABET:
17
    orgCharts[letter] = OrgChart(letter)
18
orgCharts['A'].addDirectReports([
19
    orgCharts['B'],
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
