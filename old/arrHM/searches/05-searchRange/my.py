def searchForRange(arr, target):
    # Write your code here.
	idx = binarySearch(arr, 0, len(arr) - 1, target)
	if idx == -1:
		return [-1, -1]
	else:
		minIdx = idx
		while minIdx - 1 >= 0 and arr[minIdx - 1] == arr[idx]:
			minIdx -= 1
		maxIdx = idx
		while maxIdx + 1 <= len(arr) - 1 and arr[maxIdx + 1] == arr[idx]:
			maxIdx += 1
		return [minIdx, maxIdx]


def binarySearch(arr, si, ei, target):
	if si > ei:
		return -1
	mid = si + (ei - si) // 2
	if arr[mid] < target:
		return binarySearch(arr, mid + 1, ei, target)
	elif target < arr[mid]:
		return binarySearch(arr, si, mid - 1, target)
	else:
		return mid
