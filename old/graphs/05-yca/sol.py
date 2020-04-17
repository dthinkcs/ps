
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
Youngest Common Ancestor
​
You're given three inputs, all of which are instances of a class that have an "ancestor" property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor), and the other two inputs are descendants in the ancestral tree. Write a function that returns the youngest common ancestor to the two descendants.
​
Sample input: Node A, Node E, Node I (from the ancestral tree below)
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
# O(d) time | O(1) space - where d is the depth (height) of the ancestral tree
4
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
5
    depthOne = getDescendantDepth(descendantOne, topAncestor)
6
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
7
    if depthOne > depthTwo:
8
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
9
    else:
10
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)
11
​
12
def getDescendantDepth(descendant, topAncestor):
13
    depth = 0
14
    while descendant != topAncestor:
15
        depth += 1
16
        descendant = descendant.ancestor
17
    return depth
18
​
19
def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
20
    while diff > 0:
21
        lowerDescendant = lowerDescendant.ancestor
22
        diff -= 1
23
    while lowerDescendant != higherDescendant:
24
        lowerDescendant = lowerDescendant.ancestor
25
        higherDescendant = higherDescendant.ancestor
26
    return lowerDescendant
Help:Hide
Show
Hint #1Hint #2Optimal Space & Time Complexity
You could try to simultaneously iterate through the ancestors of both input descendants until you find a common ancestor; however, if one of the descendants has more ancestors than the other (i.e., is lower in the ancestral tree), you won't find the youngest common ancestor. How can you get around this problem?
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
class AncestralTree:
6
    def __init__(self, name):
7
        self.name = name
8
        self.ancestor = None
9
​
10
    def addAsAncestor(self, descendants):
11
        for descendant in descendants:
12
            descendant.ancestor = self
13
​
14
ancestralTrees = {}
15
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
16
for letter in ALPHABET:
17
    ancestralTrees[letter] = AncestralTree(letter)
18
ancestralTrees['A'].addAsAncestor([
19
    ancestralTrees['B'],
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
