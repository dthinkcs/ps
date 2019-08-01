def quickselect(arr, k):
	return quickSort(arr, 0, len(arr) - 1, k)

def quickSort(arr, si, ei, k):
	if si > ei:
		return None

	# find all numbers smaller than that number
	count = 0
	for i in range(si, ei + 1):
		if arr[i] < arr[si]:
			count += 1
	pivot = count + si # imp BUG possibility
	if pivot == k - 1:
		return arr[si]
	arr[pivot], arr[si] = arr[si], arr[pivot]
	leftIdx = si
	rightIdx = ei
	while True:
		if leftIdx >= pivot or rightIdx <= pivot:
			break
		if arr[leftIdx] >= arr[pivot] and arr[pivot] > arr[rightIdx]:
			arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
			leftIdx +=1
			rightIdx -= 1
		elif arr[leftIdx] >= arr[pivot]:
			rightIdx -= 1
		else:
			leftIdx += 1

	leftAns = quickSort(arr, si, pivot - 1, k)
	rightAns = quickSort(arr, pivot + 1, ei, k)
	if leftAns:
		return leftAns
	if rightAns:
		return rightAns
	return None
