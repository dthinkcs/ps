
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
Min Rewards
​
Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: first, all students must receive at least one reward; second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score. Assume that all students have different scores; in other words, the scores are all unique. Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the while satisfying the two rules.
​
Sample input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])
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
# O(n) time | O(n) space - where in is the length of the input array
4
def minRewards(scores):
5
    rewards = [1 for _ in scores]
6
    localMinIdxs = getLocalMinIdxs(scores)
7
    for localMinIdx in localMinIdxs:
8
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
9
    return sum(rewards)
10
​
11
def getLocalMinIdxs(array):
12
    if len(array) == 1:
13
        return [0]
14
    localMinIdxs = []
15
    for i in range(len(array)):
16
        if i == 0 and array[i] < array[i + 1]:
17
            localMinIdxs.append(i)
18
        if i == len(array) - 1 and array[i] < array[i - 1]:
19
            localMinIdxs.append(i)
20
        if i == 0 or i == len(array) - 1:
21
            continue
22
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
23
            localMinIdxs.append(i)
24
    return localMinIdxs
25
​
26
def expandFromLocalMinIdx(localMinIdx, scores, rewards):
27
    leftIdx = localMinIdx - 1
28
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
29
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
30
        leftIdx -= 1
31
    rightIdx = localMinIdx + 1
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
You could try iterating through the input list of scores and incrementing the number of rewards you give to each student if they have a greater score than the previous student's score. However, if you reach a student with a smaller score than the previous student's score, you'll have to backtrack through the array to fix previous reward assignments. During this backtrack, is it correct to simply increment the reward of a student whose score is greater than the next student's score?
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
        self.assertEqual(program.minRewards([1]), 1)
9

10
    def test_case_2(self):
11
        self.assertEqual(program.minRewards([5, 10]), 3)
12

13
    def test_case_3(self):
14
        self.assertEqual(program.minRewards([10, 5]), 3)
15
​
16
    def test_case_4(self):
17
        self.assertEqual(program.minRewards([4, 2, 1, 3]), 8)
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
