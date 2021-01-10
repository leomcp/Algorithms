


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BSTree:
	def __init__(self):
		self.root = None

	def get_root(self):
		if self.root:
			return self.root

	def insert(self, node_data):
		if self.root is None:
			self.root = Node(node_data)
		else:
			self._insert(self.root, self.data)

	def _insert(self, curr_node, node_data):
		if curr_node.data > node_data:
			if curr_node.left is None:
				curr_node.left = Node(node_data)
			else:
				self._insert(curr_node.left, node_data)
		elif curr_node.data < node_data:
			if curr_node.right is None:
				curr_node.right = Node(node_data)
			else:
				self._insert(curr_node.right, node_data)
		else:
			print("ALready inserted Node")

	def inorder(self):
		if self.root:
			self._inorder(self.root)
			print()

	def _inorder(curr_node):
		if curr_node:
			self._inorder(curr_node.left)
			print(curr_node.data, end=" ")
			self._inorder(curr_node.right)

def find_identical(self, root1, root2):

	if root1 is None and root2 is None:
		return 1 
	if root1 is not None and root2 is not None:
		if root1.data == root2.data and 
		find_identical(root1.left, root2.left) and
		find_identical(root1.right, root2.right)

	return False 


if __name__ == "__main__":

	bst = BSTree()

	in_put = [10, 8, 15, 2, 9, 13, 18]

	for elem in in_put:
		bst.inorder()

	print()
	bst.inorder()

	is_identical(bst.get_root, bst.get_root)
