umberSum(array, targetSum):
5
    for i in range(len(array) - 1):
6
        firstNum = array[i]
7
        for j in range(i + 1, len(array)):
8
            secondNum = array[j]
9
            if firstNum + secondNum == targetSum:
10
                return sorted([firstNum, secondNum])
11
    return []
12
​
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(n) time | O(n) space
4
def twoNumberSum(array, targetSum):
5
    nums = {}
6
    for num in array:
7
        potentialMatch = targetSum - num
8
        if potentialMatch in nums:
9
            return sorted([potentialMatch, num])
10
        else:
11
            nums[num] = True
12
    return []


​
3
# O(nlog(n)) | O(1) space
4
def twoNumberSum(array, targetSum):
5
    array.sort()
6
    left = 0
7
    right = len(array) - 1
8
    while left < right:
9
        currentSum = array[left] + array[right]
10
        if currentSum == targetSum:
11
            return [array[left], array[right]]
12
        elif currentSum < targetSum:
13
            left += 1
14
        elif currentSum > targetSum:
15
            right -= 1
16
    return []
17
​

25
    def test_case_6(self):
26
        self.assertEqual(program.twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18), [3, 15])
27

28
    def test_case_7(self):
29
        self.assertEqual(program.twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5), [-5, 0])
30

31
    def test_case_8(self):
32
        self.assertEqual(program.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163), [-47, 210])
33

34
    def test_case_9(self):
35
        self.assertEqual(program.twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164), [])
36

37
    def test_case_10(self):
38
        self.assertEqual(program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15), [])
39

40
​
41
if __name__ == "__main__":
42
    unittest.main()
43
​
44
​
