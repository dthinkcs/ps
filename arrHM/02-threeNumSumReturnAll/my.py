def threeNumberSum(arr, targetSum):
    # Write your code here.
	arrArr = []
	for i in range(len(arr) - 1):
		#newArr =  arr[i + 1:]
		seen = set()
		for j in range(i + 1, len(arr)):
			if targetSum - arr[i] - arr[j] in seen:
				arrArr.append(sorted([targetSum - arr[i] - arr[j], arr[i], arr[j]]))
			seen.add(arr[j])

	return sorted(arrArr)
