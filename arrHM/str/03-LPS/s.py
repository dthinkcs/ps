
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
Longest Palindromic Substring
​
Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that is written the same forward and backward. Assume that there will only be one longest palindromic substring.
​
Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"
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
# O(n^3) time | O(1) space
4
def longestPalindromicSubstring(string):
5
    longest = "";
6
    for i in range(len(string)):
7
        for j in range(i, len(string)):
8
            substring = string[i:j + 1]
9
            if len(substring) > len(longest) and isPalindrome(substring):
10
                longest = substring
11
    return longest
12
​
13
def isPalindrome(string):
14
    leftIdx = 0
15
    rightIdx = len(string) - 1
16
    while leftIdx < rightIdx:
17
        if string[leftIdx] != string[rightIdx]:
18
            return False
19
        leftIdx += 1
20
        rightIdx -= 1
21
    return True
22
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try generating all possible substrings of the input string and checking for their palindromicity. What is the runtime of the isPalindrome check? What is the total runtime of this approach?
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
        self.assertEqual(program.longestPalindromicSubstring("a"), "a")
9

10
    def test_case_2(self):
11
        self.assertEqual(program.longestPalindromicSubstring("it's highnoon"), "noon")
12

13
    def test_case_3(self):
14
        self.assertEqual(program.longestPalindromicSubstring("noon high it is"), "noon")
15

16
    def test_case_4(self):
17
        self.assertEqual(program.longestPalindromicSubstring("abccbait's highnoon"), "abccba")
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
Longest Palindromic Substring
​
Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that is written the same forward and backward. Assume that there will only be one longest palindromic substring.
​
Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"
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
# O(n^2) time | O(1) space
4
def longestPalindromicSubstring(string):
5
    currentLongest = [0, 1]
6
    for i in range(1, len(string)):
7
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
8
        even = getLongestPalindromeFrom(string, i - 1, i)
9
        longest = max(odd, even, key = lambda x: x[1] - x[0])
10
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
11
    return string[currentLongest[0]:currentLongest[1]]
12
​
13
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
14
    while leftIdx >= 0 and rightIdx < len(string):
15
        if string[leftIdx] != string[rightIdx]:
16
            break
17
        leftIdx -= 1
18
        rightIdx += 1
19
    return [leftIdx + 1, rightIdx]
20
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try generating all possible substrings of the input string and checking for their palindromicity. What is the runtime of the isPalindrome check? What is the total runtime of this approach?
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
        self.assertEqual(program.longestPalindromicSubstring("a"), "a")
9

10
    def test_case_2(self):
11
        self.assertEqual(program.longestPalindromicSubstring("it's highnoon"), "noon")
12

13
    def test_case_3(self):
14
        self.assertEqual(program.longestPalindromicSubstring("noon high it is"), "noon")
15

16
    def test_case_4(self):
17
        self.assertEqual(program.longestPalindromicSubstring("abccbait's highnoon"), "abccba")
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
