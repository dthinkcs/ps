def largestRange(arr):
    # Write your code here.
	visited = dict()
	for num in arr:
		visited[num] = False

	ranges = [0, 0]
	maxRanges = [0, 0]
	for num in arr:
		if not visited[num]:
			temp = num
			visited[num] = True
			while True:
				if num + 1 not in arr:
					ranges[1] = num
					break
				else:
					visited[num + 1] = True
				num += 1


			while True:
				if temp - 1 not in arr:
					ranges[0] = temp
					break
				else:
					visited[temp - 1] = True
				temp -= 1

		if (ranges[1] - ranges[0]) >= (maxRanges[1] - maxRanges[0]):
			maxRanges = ranges[:]

	return maxRanges
