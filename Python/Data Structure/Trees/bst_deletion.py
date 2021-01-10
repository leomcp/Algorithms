
class Node:

	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None
		self.parent = None

class BSTree:

	def __init__(self):
		self.root = None

	def get_Root(self):
		return self.root.data 

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(self.root, data)

	def _insert(self, curr_node, data):
		if curr_node.data > key:
			if curr_node.left is None:
				curr_node.left = Node(data)
				curr_node.left.parent = curr_node
			else:
				self._insert(curr_node.left, data)
		elif curr_node.data < key:
			if curr_node.right is None:
				curr_node.right =Node(data)
				curr_node.right.parent = curr_node
			else:
				self._insert(curr_node.right, data)

	def inOrder(self):
		if self.root:
			print("InOrder Traversal :")
			self._inOrder(self.root)
			print()

	def _inOrder(self, curr_node):
		if curr_node:
			self._inOrder(curr_node.left)
			print(curr_node.data, end=" ")
			self._inOrder(curr_node.right)

	def find(self, key):
		if self.root:
			return self._find(self.root, key)

	def _find(self, curr_node, key):
		if curr_node.data == key:
			return curr_node
		elif curr_node.data > key and curr_node.left !=None:
			return self._find(curr_node.left, key)
		elif curr_node.data < key and curr_node.right != None:
			return self._find(curr_node.right, key)
		else:
			print("{} Not Found".format(key))

	def delete(self, key):
		if self.root:
			print("-"*50)
			print("Deletion of {}".format(key))
			self._delete_Node(self.find(key))
			self.inOrder()


	def _delete_Node(self, node):
		if node is None:
			print("Node to be delete does not exist in given Tree")
			return 

		def n_Child(node):
			n_child = 0

			if node.left is not None:
				n_child += 1
			if node.right is not None:
				n_child += 1 
			return n_child 

		def inOrderSuccessor(node):
			curr_node = node

			while curr_node.left is not None:
				curr_node = curr_node.left 
			return curr_node

		parent_node = node.parent 
		n_child = n_Child(node)

		if n_child == 0:
			if parent_node is not None:
				if parent_node.left == node:
					parent_node.left = None
				else:
					parent_node.right = None
			else:
				self.root = None

		if n_child == 1:
			if node.left is not None:
				child = node.left
			else:
				child = node.right

			if parent_node is not None:
				if parent_node.left == node:
					parent_node.left = child 
				else:
					parent_node.right = child 
			else:
				self.root = child 

		if n_child == 2:
			successor = inOrderSuccessor(node.right)
			node.data = successor.data 
			self._delete_Node(successor)

if __name__ == "__main__":

	t = BSTree()

	in_data = [50, 30, 70, 20, 40, 60, 80]

	for key in in_data:
		t.insert(key)

	print("Root : {}".format(t.get_Root()))

	t.inOrder()

	t.delete(100)

	t.delete(20)

	t.delete(30)

	t.delete(50)


""" 

OUTPUT : 

Root : 50
InOrder Traversal :
20 30 40 50 60 70 80 
--------------------------------------------------
Deletion of 100
100 Not Found
Node to be delete does not exist in given Tree
InOrder Traversal :
20 30 40 50 60 70 80 
--------------------------------------------------
Deletion of 20
InOrder Traversal :
30 40 50 60 70 80 
--------------------------------------------------
Deletion of 30
InOrder Traversal :
40 50 60 70 80 
--------------------------------------------------
Deletion of 50
InOrder Traversal :
40 60 70 80 


"""




