
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
Continuous Median
​
Write a class that can support the following two functionalities: 1) the continuous insertion of numbers and 2) the instant (O(1) time) retrieval of the median of the numbers that have been inserted thus far. The getMedian() method, which handles the retrieval of the median, has already been written for you. You simply have to write the insert() method.
​
Sample input: insert(5), insert(10), getMedian(), insert(100), getMedian()
Sample output: -, -, 7.5, -, 10
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
class ContinuousMedianHandler:
4
    def __init__(self):
5
        self.lowers = Heap(MAX_HEAP_FUNC, [])
6
        self.greaters = Heap(MIN_HEAP_FUNC, [])
7
        self.median = None
8
​
9
    # O(log(n)) time | O(n) space
10
    def insert(self, number):
11
        if not self.lowers.length or number < self.lowers.peek():
12
            self.lowers.insert(number)
13
        else:
14
            self.greaters.insert(number)
15
        self.rebalanceHeaps()
16
        self.updateMedian()
17
​
18
    def rebalanceHeaps(self):
19
        if self.lowers.length - self.greaters.length == 2:
20
            self.greaters.insert(self.lowers.remove())
21
        elif self.greaters.length - self.lowers.length == 2:
22
            self.lowers.insert(self.greaters.remove())
23
​
24
​
25
    def updateMedian(self):
26
        if self.lowers.length == self.greaters.length:
27
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
28
        elif self.lowers.length > self.greaters.length:
29
            self.median = self.lowers.peek()
30
        else:
31
            self.median = self.greaters.peek()
32
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
The median of a set of numbers is often, by definition, one of the numbers in the set. Thus, you likely have to store all of the inserted numbers somewhere to be able to continuously compute their median.
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
test = program.ContinuousMedianHandler()
6
​
7
​
8
class TestProgram(unittest.TestCase):
9
​
10
    def test_case_1(self):
11
        test.insert(5)
12
        self.assertEqual(test.getMedian(), 5)
13
        test.insert(10)
14
        self.assertEqual(test.getMedian(), 7.5)
15
​
16
    def test_case_2(self):
17
        test.insert(100)
18
        self.assertEqual(test.getMedian(), 10)
19
        test.insert(200)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
