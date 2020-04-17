
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
Multi String Search
​
Write a function that takes in a "big" string and an array of "small" strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether or not the small string at that index in the array of small strings is contained in the big string. Note that you cannot use language-built-in string-matching methods.
​
Sample input: "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample output: [True, False, True, True, False, True, False]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(bns) time | O(n) space
4
def multiStringSearch(bigString, smallStrings):
5
    return [isInBigString(bigString, smallString) for smallString in smallStrings]
6
​
7
def isInBigString(bigString, smallString):
8
    for i in range(len(bigString)):
9
        if i + len(smallString) > len(bigString):
10
            break
11
        if isInBigStringHelper(bigString, smallString, i):
12
            return True
13
    return False
14
​
15
def isInBigStringHelper(bigString, smallString, startIdx):
16
    leftBigIdx = startIdx
17
    rightBigIdx = startIdx + len(smallString) - 1
18
    leftSmallIdx = 0
19
    rightSmallIdx = len(smallString) - 1
20
    while leftBigIdx <= rightBigIdx:
21
        if (
22
            bigString[leftBigIdx] != smallString[leftSmallIdx] or
23
            bigString[rightBigIdx] != smallString[rightSmallIdx]
24
            ):
25
            return False
26
        leftBigIdx += 1
27
        rightBigIdx -= 1
28
        leftSmallIdx += 1
29
        rightSmallIdx -= 1
30
    return True
31
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
A simple way to solve this problem is to iterate through all of the small strings, checking if each of them is contained in the big string by iterating through the big string's characters and comparing them to the given small string's characters with a couple of loops. Is this approach efficient from a time-complexity point of view?
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
        self.assertEqual(program.multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]), [True, False, True, True, False, True, False])
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]), [True, True, False, True, True, False, False])
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.multiStringSearch("adcb akfkw afnmc fkadn vkaca jdaf dacb cdba cbda", ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]), [False, False, False, False, True, False, False])
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.multiStringSearch("test testing testings tests testers test-takers", ["tests", "testatk", "testiing", "trsatii", "test-taker", "test"]), [True, False, False, False, True, True])
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
Multi String Search
​
Write a function that takes in a "big" string and an array of "small" strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether or not the small string at that index in the array of small strings is contained in the big string. Note that you cannot use language-built-in string-matching methods.
​
Sample input: "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample output: [True, False, True, True, False, True, False]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(b^2 + ns) time | O(b^2 + n) space
4
def multiStringSearch(bigString, smallStrings):
5
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
6
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]
7
​
8
class ModifiedSuffixTrie:
9
    def __init__(self, string):
10
        self.root = {}
11
        self.populateModifiedSuffixTrieFrom(string)
12
​
13
    def populateModifiedSuffixTrieFrom(self, string):
14
        for i in range(len(string)):
15
            self.insertSubstringStartingAt(i, string)
16
​
17
    def insertSubstringStartingAt(self, i, string):
18
        node = self.root
19
        for j in range(i, len(string)):
20
            letter = string[j]
21
            if letter not in node:
22
                node[letter] = {}
23
            node = node[letter]
24
​
25
    def contains(self, string):
26
        node = self.root
27
        for letter in string:
28
            if letter not in node:
29
                return False
30
            node = node[letter]
31
        return True
32
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
A simple way to solve this problem is to iterate through all of the small strings, checking if each of them is contained in the big string by iterating through the big string's characters and comparing them to the given small string's characters with a couple of loops. Is this approach efficient from a time-complexity point of view?
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
        self.assertEqual(program.multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]), [True, False, True, True, False, True, False])
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]), [True, True, False, True, True, False, False])
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.multiStringSearch("adcb akfkw afnmc fkadn vkaca jdaf dacb cdba cbda", ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]), [False, False, False, False, True, False, False])
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.multiStringSearch("test testing testings tests testers test-takers", ["tests", "testatk", "testiing", "trsatii", "test-taker", "test"]), [True, False, False, False, True, True])
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
Multi String Search
​
Write a function that takes in a "big" string and an array of "small" strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether or not the small string at that index in the array of small strings is contained in the big string. Note that you cannot use language-built-in string-matching methods.
​
Sample input: "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample output: [True, False, True, True, False, True, False]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2Solution #3
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(ns + bs) time | O(ns) space
4
def multiStringSearch(bigString, smallStrings):
5
    trie = Trie()
6
    for string in smallStrings:
7
        trie.insert(string)
8
    containedStrings = {}
9
    for i in range(len(bigString)):
10
        findSmallStringsIn(bigString, i, trie, containedStrings)
11
    return [string in containedStrings for string in smallStrings]
12
​
13
​
14
def findSmallStringsIn(string, startIdx, trie, containedStrings):
15
    currentNode = trie.root
16
    for i in range(startIdx, len(string)):
17
        currentChar = string[i]
18
        if currentChar not in currentNode:
19
            break
20
        currentNode = currentNode[currentChar]
21
        if trie.endSymbol in currentNode:
22
            containedStrings[currentNode[trie.endSymbol]] = True
23
​
24
class Trie:
25
    def __init__(self):
26
        self.root = {}
27
        self.endSymbol = "*"
28
​
29
    def insert(self, string):
30
        current = self.root
31
        for i in range(len(string)):
32
            if string[i] not in current:
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
A simple way to solve this problem is to iterate through all of the small strings, checking if each of them is contained in the big string by iterating through the big string's characters and comparing them to the given small string's characters with a couple of loops. Is this approach efficient from a time-complexity point of view?
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
        self.assertEqual(program.multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]), [True, False, True, True, False, True, False])
9
​
10
    def test_case_2(self):
11
        self.assertEqual(program.multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]), [True, True, False, True, True, False, False])
12
​
13
    def test_case_3(self):
14
        self.assertEqual(program.multiStringSearch("adcb akfkw afnmc fkadn vkaca jdaf dacb cdba cbda", ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]), [False, False, False, False, True, False, False])
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.multiStringSearch("test testing testings tests testers test-takers", ["tests", "testatk", "testiing", "trsatii", "test-taker", "test"]), [True, False, False, False, True, True])
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
