# import copy
# value, weight
def knapsackProblem(items, capacity):
    # Write your code here.

	# 0 ... maxCapacity  dp === maxValueExtraction
	# dp = [ [ 0 ] * (capacity + 1) ] * (len(items) + 1)
	foo = [0, []]
	dp = [[(foo) for x in range(capacity + 1)] for y in range(len(items) + 1)]

	for i in range(1, len(dp)):

		for j in range(1, len(dp[0])):
			# leave it
			option1 = ( [ dp[i - 1][j][0],  dp[i - 1][j][1][:]] )
			#print(option1)
			# take it
			option2 = [ 0, [] ]

			jback = j - items[i - 1][1]
			if jback >= 0:
				option2 =  ( [ dp[i - 1][ jback ][0] + items[i - 1][0], dp[i - 1][ jback ][1][:] + [ i - 1 ] ] )
			#print(option2)
			# dp[i][j] = max of whatever is there
			if option1[0] >= option2[0]:
				dp[i][j] = option1
			else:
				dp[i][j] = option2
			#print(dp)

	return dp[-1][-1]
	

def printDP(dp):
	for r in dp:
		for v in r:
			print(v, end=" ")
		print()


print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
