def bubbleSort(arr):
    # Write your code here.

	for i in range(len(arr) - 1):
		isSorted = True
		for j in range(len(arr) - 1):
			if arr[j] > arr[j + 1]:
				isSorted = False
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if isSorted:
			break

	return arr
	
