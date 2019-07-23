
def maxSumWithRoot(root, maxArr):

	if root == None:
		return 0
	ml = maxSumWithRoot(root.left, maxArr)
	mr = maxSumWithRoot(root.right, maxArr)
	retVal = max(ml + root.value, mr + root.value, root.value)
	maxArr[0] = max(maxArr[0], ml, retVal, mr, ml + mr + root.value)
	return retVal

def maxPathSum(tree):
    # Write your code here.
	maxArr = [float('-inf')]
	#ALSO correct return max(maxSumWithRoot(tree, maxArr), maxArr[0])
	#NOT corr max(maxArr[0], maxSumWithRoot(tree, maxArr),) BUG BUG BUG
	maxSumWithRoot(tree, maxArr)
	return maxArr[0]
