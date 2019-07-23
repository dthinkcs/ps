def subarraySort(arr):
    # Write your code here. BUGS : 1.firstIdx = -1... 2.break statement 3. <= equality symbol 4. for range(le -1 minus 1 , zero, minus 1 )

	# find the numbers which are not sorted first Indices of them
	firstIdx = -1
	secondIdx = -1
	for i in range(len(arr) - 1):
		if arr[i] <= arr[i + 1]:
			continue
		firstIdx = i
		break

	for i in range(len(arr) - 1, 0, -1):
		if arr[i - 1] <= arr[i]:
			continue
		secondIdx = i
		break
	# out of those numbers find the minimum number, maximum number
	startIdx = -1
	endIdx = -1
	tempArr = arr[firstIdx: secondIdx + 1]
	if len(tempArr):
		minima = min(tempArr)
		maxima = max(tempArr)
	# see where the minimum number goes, maximum number goes by comparing it to every element from the start, end respectively

		for i in range(len(arr)):
			if minima < arr[i]:
				startIdx = i
				break
		for i in range(len(arr) - 1, 0, -1):
			if maxima > arr[i]:
				endIdx = i
				break

	return [startIdx, endIdx]
