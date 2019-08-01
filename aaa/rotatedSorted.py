def shiftedBinarySearch(arr, target):
    # Write your code here.
	start = 0
	end = len(arr) - 1
	pivot = -1
	# find the pivot elemeent
	while start <= end:
		mid = start + (end - start) // 2
		if arr[mid] > arr[mid + 1]:
			pivot = mid + 1
			break
		elif arr[start] <= arr[mid]: # TODO pivot is not going to be there 45 ..45 vs .. 45 45
			start = mid + 1
		else:
			end = mid - 1

	if pivot == -1:
		return binarySearch(arr, 0, len(arr) - 1, target)
	else:
		left = binarySearch(arr, 0, pivot - 1, target)
		if left != -1:
			return left
		right = binarySearch(arr, pivot, len(arr) - 1, target)
		if right != -1:
			return right
		return -1

def binarySearch(arr, si, ei, target):
	if si > ei:
		return -1

	mid = si + (ei - si) // 2
	if arr[mid] < target:
		return binarySearch(arr, mid + 1, ei, target)
	elif arr[mid] > target:
		return binarySearch(arr, si, mid - 1, target)
	else:
		return mid
