def depth(node):
	d = 0
	while node.ancestor != None:
		d += 1
		node = node.ancestor
	return d

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	depthOne = depth(descendantOne)
	depthTwo = depth(descendantTwo)
	if depthOne < depthTwo:
		descLess = descendantOne
		depthLess = depthOne
		descMore = descendantTwo
		depthMore = depthTwo
	else:
		descLess = descendantTwo
		depthLess = depthTwo
		descMore = descendantOne
		depthMore = depthOne

	if depthLess == 0:
		return topAncestor

	while depthMore != depthLess:
		descMore = descMore.ancestor
		depthMore -= 1

	while descMore != descLess: # BUG was here descMore.ancestor != descLess.ancestor # return
		descMore = descMore.ancestor
		descLess = descLess.ancestor
	return descMore

	
