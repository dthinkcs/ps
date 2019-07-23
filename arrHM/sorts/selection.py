def selectionSort(arr):
    # Write your code here.
	for i in range(len(arr) - 1):
		minPos = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[minPos]:
				minPos = j
		arr[i], arr[minPos] = arr[minPos], arr[i]
	return arr
