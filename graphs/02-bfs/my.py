class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
		q = [self]
		while len(q) > 0:
			frontNode = q.pop(0)
			array.append(frontNode.name)
			for child in frontNode.children:
				q.append(child)
		return array
