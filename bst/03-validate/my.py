# ThIS IS not OPTIMAL 4 * going down WISW
def validateBst(tree):
    # Write your code here.
	if tree is None:
		return True
    # this BST HAS REPEATED ELEMENTS  AND AND AND equality only to left
	return getMax(tree.left) < tree.value <= getMin(tree.right) and validateBst(tree.left) and validateBst(tree.right)

def getMax(tree):
	if tree is None:
		return float('-inf')
	if tree.right is None:
		return tree.value
	return getMax(tree.right)

def getMin(tree):
	if tree is None:
		return float('inf')
	if tree.left is None:
		return tree.value
	return getMin(tree.left)
