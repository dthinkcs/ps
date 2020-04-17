
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
Four Number Sum
​
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should return an empty array.
​
Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
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
# Average: O(n^2) time | O(n^2) space
4
# Worst: O(n^3) time | O(n^2) space
5
def fourNumberSum(array, targetSum):
6
    allPairSums = {}
7
    quadruplets = []
8
    for i in range(1, len(array) - 1):
9
        for j in range(i + 1, len(array)):
10
            currentSum = array[i] + array[j]
11
            difference = targetSum - currentSum
12
            if difference in allPairSums:
13
                for pair in allPairSums[difference]:
14
                    quadruplets.append(pair + [array[i], array[j]])
15
        for k in range(0, i):
16
            currentSum = array[i] + array[k]
17
            if currentSum not in allPairSums:
18
                allPairSums[currentSum] = [[array[k], array[i]]]
19
            else:
20
                allPairSums[currentSum].append([array[k], array[i]])
21
    return quadruplets
22
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Using four for loops to calculate the sums of all possible quadruplets in the array would generate an algorithm that runs in O(n^4) time, where n is the length of the input array. Can you come up with something faster using fewer for loops?
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
def sortAndStringify(array):
6
    return ",".join(sorted(list(map(lambda x: str(x), array))))
7
​
8
​
9
class TestProgram(unittest.TestCase):
10
​
11
    def test_case_1(self):
12
        output = program.fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10)
13
        output = list(map(sortAndStringify, output))
14
        quadruplets = [
15
            [1, 2, 3, 4],
16
        ]
17
        self.assertTrue(len(output) == 1)
18
        for quadruplet in quadruplets:
19
            self.assertTrue(sortAndStringify(quadruplet) in output)
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
