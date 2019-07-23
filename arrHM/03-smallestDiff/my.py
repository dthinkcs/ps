def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	A = sorted(arrayOne)
	B = sorted(arrayTwo)
	i = 0
	j = 0
	smallestDiff = float('inf')
	while i < len(A) and j < len(B):
		currDiff = abs(A[i] - B[j])
		if currDiff < smallestDiff:
			ans = [A[i], B[j]]
			smallestDiff = currDiff
		# update condition
		if A[i] < B[j]:
			i += 1
		else:
			j += 1

	return ans
