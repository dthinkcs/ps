
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
Subarray Sort
​
Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return [-1, -1].
​
Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample output: [3, 9]
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
# O(n) time | O(1) space
4
def subarraySort(array):
5
    minOutOfOrder = float("inf")
6
    maxOutOfOrder = float("-inf")
7
    for i in range(len(array)):
8
        num = array[i]
9
        if isOutOfOrder(i, num, array):
10
            minOutOfOrder = min(minOutOfOrder, num)
11
            maxOutOfOrder = max(maxOutOfOrder, num)
12
    if minOutOfOrder == float("inf"):
13
        return [-1, -1]
14
    subarrayLeftIdx = 0
15
    while minOutOfOrder >= array[subarrayLeftIdx]:
16
        subarrayLeftIdx += 1
17
    subarrayRightIdx = len(array) - 1
18
    while maxOutOfOrder <= array[subarrayRightIdx]:
19
        subarrayRightIdx -= 1
20
    return [subarrayLeftIdx, subarrayRightIdx]
21
​
22
def isOutOfOrder(i, num, array):
23
    if i == 0:
24
        return num > array[i + 1]
25
    if i == len(array) - 1:
26
        return num < array[i - 1]
27
    return num > array[i + 1] or num < array[i - 1]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subarraySort([1, 2]), [-1, -1])

    def test_case_2(self):
        self.assertEqual(subarraySort([2, 1]), [0, 1])

    def test_case_3(self):
        self.assertEqual(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test_case_4(self):
        self.assertEqual(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]), [4, 9])

unittest.main()
