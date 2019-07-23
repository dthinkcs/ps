def kadanesAlgorithm(arr):
    # Write your code here.
	if max(arr) <= 0:
		return max(arr)

	maxAns = 0
	currAns = 0
	for i in range(len(arr)):

		if currAns + arr[i] < 0: # BUG2 leaving out currAns taking the entire thing like 		if currAns + arr[i] < 0: # BUG2 leaving out currAns taking the entire thing like
			currAns = 0 # BUG1  = arr[i]
		else:
			currAns += arr[i]

		if currAns > maxAns:
			maxAns = currAns

	return maxAns
