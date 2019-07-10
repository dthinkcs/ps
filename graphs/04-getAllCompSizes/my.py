def riverSizes(matrix):
    # Write your code here.
	lt = []
	visited = [ [False for ele in row] for row in matrix ]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1 and not visited[i][j]:
				lt.append(sizeOfComp(i, j, matrix, visited))

	return sorted(lt)

#dis = [-1, 0, 1] # i   i   i-1 i + 1
#djs = [-1, 0, 1] # j-1 j+1 j   j
didjs = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
def sizeOfComp(i, j, matrix, visited):
	visited[i][j] = True
	smallSize = 0
	for di, dj in didjs: #for dj in djs:
		nextI = i + di
		nextJ = j + dj
		if nextI == i and nextJ == j:
			continue
		if isValid(nextI, nextJ, matrix) and matrix[nextI][nextJ] == 1 and not visited[nextI][nextJ]:
			smallSize += sizeOfComp(nextI, nextJ, matrix, visited)
	return 1 + smallSize

def isValid(i, j, matrix):
	return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])
