# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
		# 4
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)
	# set the node to tail i.e. take it out of the dll and kinda pushit to the tail
    def setTail(self, node):
        # Write your code here.
		# 5
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
		# 3 NOW NOW NOW
        # Write your code here.
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert) # remove the node to insert
		# Duplication/replication (ex 2 is node and 3 is nodeToInsert)
		nodeToInsert.next = node # 1 - 2 - 3 - 4 if the 3 has to come become 3 -2
		nodeToInsert.prev = node.prev
		# Mutation
		# BUG part must be mirrir / Prev before next COZ
		# node.prev = nodeToInsert IF YOU CHANGE prev IT BECOMES INACCESSIBLE
		if node.prev:
			node.prev.next = nodeToInsert # 1- 3
		else:
			self.head = nodeToInsert
		node.prev = nodeToInsert




    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		# THIS WAS THE BUG
		#if node == self.head and node == self.tail:
			#return
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next:
			node.next.prev = nodeToInsert
		else:
			self.tail = nodeToInsert
		node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
		if position == 1:
			self.setHead(nodeToInsert)
			return
		pos = 1
		node = self.head
		while node and pos != position:
			node = node.next
			pos += 1
		if node: # or pos == position
			# BUG SEE IT BEFORE/after TYPING self.insertAfter(node, nodeToInsert)
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)



	# REMOVE ALL VALUES
    def removeNodesWithValue(self, value):
        # Write your code here.
			# set the node to tail i.e. take it out of the dll and kinda pushit to the tail

		node = self.head
		# while node and node.value != value:
		# 	node = node.next # move forward
		# if node is not None:
		# 	self.remove(node)
		while node:
			nodeToRemove = node
			node = node.next # so that the nodeToRemove ke baad ka track
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)

    def remove(self, node):
		# 2
        # given a node remove it
		# if the node is the head of the DLL then forward it
		if node == self.head:
			self.head = self.head.next
		# BUG would be elif coz it could be head and tail as well
		if node == self.tail:
			self.tail = self.tail.prev

		if node.next:
			node.next.prev = node.prev
		if node.prev:
			node.prev.next = node.next

		# extra sure
		node.next = None
		node.prev = None

	def containsHelper(self, head, value):
		if head is None:
			return False
		if head.value == value:
			return True
		return self.containsHelper(head.next, value)

    def containsNodeWithValue(self, value):
		# 1
		# for recursive methods it helps to create helper function
		return self.containsHelper(self.head, value)
		# Iterative working YES
		# node = self.head
		# while node and node.value != value:
		# 	node = node.next
		# return node is not None # BUG was node is None
