def getPermutations(arr):
    # Write your code here.

	if len(arr) == 1:
		return [[arr[0]]]
	newArr = []
	for i in range(len(arr)):
		newArr = newArr + [[arr[i]] + array for array in getPermutations(arr[:i] + arr[i + 1:])]
	return newArr
