def fn(matrix, s, e, target):
	#print(matrix, s, e)
	if e[0] < s[0] or e[1] < s[1]:
		return [-1, -1]

	if matrix[s[0]][e[1]] == target:
		return [s[0], e[1]]
	if matrix[s[0]][e[1]] < target:
		return fn(matrix, (s[0] + 1, s[1]), e, target)
	else:
		return fn(matrix, s, (e[0], e[1] - 1), target)

def searchInSortedMatrix(matrix, target):
    # Write your code here.
	return fn(matrix, (0, 0), (len(matrix) - 1 , len(matrix[0]) - 1 ), target)
