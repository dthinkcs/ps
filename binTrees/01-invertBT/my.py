def invertBinaryTree(tree):
    # Write your code here.
	if tree is None:
		return

	tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def invertBinaryTree(tree):
    q = []
    q.append(tree)
    while len(q) != 0:
        node = q.pop(0)
        node.left, node.right = node.right, node.left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
