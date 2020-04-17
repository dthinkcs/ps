def hasSingleCycle(arr):
    # Write your code here.

	currIdx = 0 # STARTING_INDEX
	numV = 0
	while numV < len(arr): # + 1:

		# if currIdx == 0 and numV == len(arr):
		#	return True
		if currIdx == 0 and numV > 0:
			return False
		numV += 1
		currIdx = getNextIdx(currIdx, arr)
	return currIdx == 0 # last thing is
	#return False

def getNextIdx(currIdx, arr):
	nextIdx = (currIdx + arr[currIdx]) % len(arr)
	return nextIdx if nextIdx >= 0 else len(arr) + nextIdx # ex: len(arr) + (-1)
