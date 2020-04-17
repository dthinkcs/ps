def searchInSortedMatrix(matrix, target):

	row = 0
	col = len(matrix[0]) - 1

	while (isValid(matrix, row, col)):
		if matrix[row][col] == target:
			return [row, col]
		elif matrix[row][col] < target:
			row += 1
		else:
			col -= 1

	return [-1, -1]

def isValid(matrix, row, col):
	return 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1 
