def insertionSort(arr):
    # Write your code here.
	for i in range(1, len(arr)):
		ele = arr[i]
		j = i - 1
		while j >= 0:
			if arr[j] < ele:
				break
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = ele # BUG WAS arr[j] = ele and swap thing

	return arr
