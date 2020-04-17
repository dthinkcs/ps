
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
Suffix Trie Construction
​
Write a class for a suffix-trie-like data structure. The class should have a "root" property set to be the root node of the trie. The class should support creation from a string and the searching of strings. The creation method (called populateSuffixTrieFrom()) will be called when the class is instantiated and should populate the "root" property of the class. Note that every string added to the trie should end with the special "endSymbol" character: "*".
​
Sample input (for creation): "babc"
Sample output (for creation):
{
  "c": {"*": True},
  "b": {
    "c": {"*": True},
    "a": {"b": {"c": {"*": True}}},
  },
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class SuffixTrie:
4
    def __init__(self, string):
5
        self.root = {}
6
        self.endSymbol = "*"
7
        self.populateSuffixTrieFrom(string)
8
​
9
    # O(n^2) time | O(n^2) space
10
    def populateSuffixTrieFrom(self, string):
11
        for i in range(len(string)):
12
            self.insertSubstringStartingAt(i, string)
13
​
14
    def insertSubstringStartingAt(self, i, string):
15
        node = self.root
16
        for j in range(i, len(string)):
17
            letter = string[j]
18
            if letter not in node:
19
                node[letter] = {}
20
            node = node[letter]
21
        node[self.endSymbol] = True
22
​
23
    # O(m) time | O(1) space
24
    def contains(self, string):
25
        node = self.root
26
        for letter in string:
27
            if letter not in node:
28
                return False
29
            node = node[letter]
30
        return self.endSymbol in node
31
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Building a suffix-trie-like data structure consists of essentially storing every suffix of a given string in a trie. To do so, iterate through the input string one character at a time and insert every substring starting at each character and ending at the end of the string into the trie.
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
word1 = "test"
6
test1 = program.SuffixTrie(word1)
7
trie1 = {
8
    "t": {
9
        "*": True,
10
        "e": {"s": {"t": {"*": True}}},
11
    },
12
    "s": {"t": {"*": True}},
13
    "e": {"s": {"t": {"*": True}}},
14
}
15
​
16
word2 = "invisible"
17
test2 = program.SuffixTrie(word2)
18
trie2 = {
19
    "e": {"*": True},
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
