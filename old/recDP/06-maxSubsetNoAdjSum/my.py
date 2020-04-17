def maxSubsetSumNoAdjacent(array):
    # Write your code here.

	if len(array) == 0:
		return 0
	return max(array[0] + maxSubsetSumNoAdjacent(array[2:]), maxSubsetSumNoAdjacent(array[1:]))

def maxSubsetSumNoAdjacent(array, memo={}):
    # Write your code here.
    if len(array) in memo:
        return memo[len(array)]
    if len(array) == 0:
        return 0
    memo[len(array)] = max(array[0] + maxSubsetSumNoAdjacent(array[2:], memo), maxSubsetSumNoAdjacent(array[1:], memo))
    return memo[len(array)]

print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]) ==  72)
