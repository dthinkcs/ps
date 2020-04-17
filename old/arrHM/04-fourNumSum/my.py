def fourNumberSum(arr, targetSum):
    # Write your code here.
	arrArr = []
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr) - 1):
			seen = set()
			yourTarget = targetSum - arr[i] - arr[j]
			for k in range(j + 1, len(arr) # BUG BUG BUG called INERTIA - 1):
				if yourTarget - arr[k] in seen:
					arrArr.append([arr[i], arr[j], arr[k], yourTarget-arr[k]])
				seen.add(arr[k])
	return arrArr

print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
