def mergeSort(arr):
    # Write your code here.
	if len(arr) <= 1:
		return arr
	else:
		mid = len(arr) // 2
		leftSorted = mergeSort(arr[:mid]) # bug was arr[:mid + 1], arr[mid + 1:]
		rightSorted = mergeSort(arr[mid:])
		return merge(leftSorted, rightSorted)

def merge(leftArr, rightArr):
	i1 = 0
	i2 = 0
	i = 0
	arr = [0] * (len(leftArr) + len(rightArr))
	while i1 < len(leftArr) and i2 < len(rightArr):
		if leftArr[i1] < rightArr[i2]:
			arr[i] = leftArr[i1]
			i1 += 1
		else:
			arr[i] = rightArr[i2]
			i2 += 1
		i += 1
	while i1 < len(leftArr):
		arr[i] = leftArr[i1]
		i += 1
		i1 += 1
	while i2 < len(rightArr):
		arr[i] = rightArr[i2]
		i += 1
		i2 += 1
	return arr
