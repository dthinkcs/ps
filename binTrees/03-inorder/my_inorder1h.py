def inorderTraversal(root):
    if root is None:
        return []
    arr = []
    stk = []
    passed = set()
    stk.append(root)
    while len(stk) != 0:
        ptr = stk[-1]
        if ptr.left and ptr not in passed: # maintain have we passed this
            stk.append(ptr.left)
            passed.add(ptr)
        else:
            node = stk.pop()
            arr.append(node.val)
            if node.right:
                stk.append(node.right)

    return arr

# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
