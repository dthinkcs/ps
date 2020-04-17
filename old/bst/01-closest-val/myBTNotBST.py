def findClosestValueInBT(tree, target):
    # Write your code here.
	if tree is None:
		return float('inf')

	leftAns = findClosestValueInBst(tree.left, target)
	rightAns = findClosestValueInBst(tree.right, target)

	minSoFar = tree.value
	if abs(leftAns - target) < abs(minSoFar - target):
		minSoFar = leftAns
	if abs(rightAns - target) < abs(minSoFar - target):
		minSoFar = rightAns
	return minSoFar

def findClosestValueInBst(tree, target):
    # Write your code here.
	if tree is None:
		return float('inf')

	if tree.value == target:
		return tree.value
	if tree.value < target:
		contender = findClosestValueInBst(tree.right, target)
	else:
		contender = findClosestValueInBst(tree.left, target)

	return tree.value if abs(tree.value - target) < abs(contender - target) else contender
