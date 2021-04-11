"""
Deletion of Node 
------------------------


"""
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
			print("-"*50)
			print("InOrder Traversal :")
			self._inOrder(self.root)
			print()

	def _inOrder(self, curr_node):
		if curr_node:
			self._inOrder(curr_node.left)
			print(curr_node.data, end=" ")
			self._inOrder(curr_node.right)

	def _height(self, curr_node, curr_height):
		if curr_node is None:
			return curr_height

		left = self._height(curr_node.left, curr_height + 1)
		right = self._height(curr_node.right, curr_height + 1)

		return max(left, right)

	def delete(self, key):
		if self.root:
			print("-"*50)
			print("Delete {} Node : ".format(key))

			node = self._findNode(self.root, key)
			if node is not None:
				self._deleteNode(node)
			else:
				print("{} Node does not exists ...".format(key))

			print("InOrder Traversal : ")
			self._inOrder(self.root)
			print()

			print("Root : {}".format(self.root.data))
			print("Height : {}".format(self._height(self.root, 0)))

	def _findNode(self, curr_node, key):
		if key == curr_node.data:
			return curr_node
		elif key > curr_node.data and curr_node.right is not None:
			return self._findNode(curr_node.right, key)
		elif key < curr_node.data and curr_node.left is not None:
			return self._findNode(curr_node.left, key)
		else:
			return None

	def _deleteNode(self, node):

		def nChild(node):
			n_child = 0
			if node.left is not None:
				n_child += 1
			if node.right is not None:
				n_child += 1
			return n_child

		def getInOrderSucc(node):
			curr_node = node.right

			while curr_node.left is not None:
				curr_node = curr_node.left

			return curr_node

		n_child = nChild(node)
		parent_n = node.parent

		if n_child == 0:
			if parent_n is not None:
				if parent_n.left == node:
					parent_n.left = None
				else:
					parent_n.right = None
			else:
				self.root = None

		if n_child == 1:
			if node.left is not None:
				child_n = node.left
			else:
				child_n = node.right

			if parent_n is not None:
				if parent_n.left == node:
					parent_n.left = child_n
					child_n.parent = parent_n
				else:
					parent_n.right= child_n
					child_n.parent = parent_n
			else:
				self.root = child_n
				child_n.parent = None

		if n_child == 2:
			nxtInOrder_n = getInOrderSucc(node)
			node.data = nxtInOrder_n.data
			self._deleteNode(nxtInOrder_n)

if __name__ == "__main__":

	t = BSTree()

	in_data = [50, 30, 70, 20, 40, 60, 80]

	for key in in_data:
		t.insert(key)

	t.inOrder()

	t.delete(100)

	t.delete(20)

	t.delete(30)

	t.delete(50)

	print("-"*50)


""" 

OUTPUT : 

--------------------------------------------------
InOrder Traversal :
20 30 40 50 60 70 80 
--------------------------------------------------
Delete 100 Node : 
100 Node does not exists ...
InOrder Traversal : 
20 30 40 50 60 70 80 
Root : 50
Height : 3
--------------------------------------------------
Delete 20 Node : 
InOrder Traversal : 
30 40 50 60 70 80 
Root : 50
Height : 3
--------------------------------------------------
Delete 30 Node : 
InOrder Traversal : 
40 50 60 70 80 
Root : 50
Height : 3
--------------------------------------------------
Delete 50 Node : 
InOrder Traversal : 
40 60 70 80 
Root : 60
Height : 3
--------------------------------------------------



"""




