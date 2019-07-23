def findClosestValueInBst(tree, target):
    # Write your code here.
	if tree is None:
		return float('inf')

	if tree.value == target:
		return target

	if tree.value < target:
		val = findClosestValueInBst(tree.right, target)
	else:
		val = findClosestValueInBst(tree.left, target)

	return val if abs(target - tree.value) > abs(target - val) else tree.value
