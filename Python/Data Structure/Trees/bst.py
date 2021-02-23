
import sys

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None
		self.hd = 0

class BSTree:

	def __init__(self):
		self.root = None

		self.level_order = []
		self.vertical_order = {}

	def buildTree(self, in_data):
		for key in in_data:
			self.insert(key)

	def insert(self, key):
		if self.root is None:
			self.root = Node(key)
		else:
			self._insert(self.root, key)

	def _insert(self, curr_node, key):
		if key > curr_node.data:
			if curr_node.right is None:
				curr_node.right = Node(key)
				curr_node.right.parent = curr_node
			else:
				self._insert(curr_node.right, key)
		elif key < curr_node.data:
			if curr_node.left is None:
				curr_node.left = Node(key)
				curr_node.left.parent = curr_node
			else:
				self._insert(curr_node.left, key)
		else:
			print("{} Node is already inserted ....".format(key))

	def getRoot(self):
		if self.root:
			print("-"*50)
			self._getRoot()

	def _getRoot(self):
			print("Root : {}".format(self.root.data))

	def inOrder(self):
		if self.root:
			print("-"*50)
			print("InOrder Traversal")
			self._inOrder(self.root)
			print()

	def _inOrder(self, curr_node):
		if curr_node:
			self._inOrder(curr_node.left)
			print(curr_node.data, end=" ")
			self._inOrder(curr_node.right)

	def preOrder(self):
		if self.root:
			print("-"*50)
			print("PreOrder Traversal")
			self._preOrder(self.root)
			print()

	def _preOrder(self, curr_node):
		if curr_node:
			print(curr_node.data, end=" ")
			self._preOrder(curr_node.left)
			self._preOrder(curr_node.right)

	def postOrder(self):
		if self.root:
			print("-"*50)
			print("PostOrder Traversal")
			self._postOrder(self.root)
			print()

	def _postOrder(self, curr_node):
		if curr_node:
			self._postOrder(curr_node.left)
			self._postOrder(curr_node.right)
			print(curr_node.data, end=" ")

	def levelOrder(self):
		if self.root:
			print("-"*50)
			print("Level Order Traversal")
			self._levelOrder()
			print()

	def _levelOrder(self):

		q = []
		q.append(self.root)
		q.append(None)

		while len(q) > 1:

			head_n = q.pop(0)

			if head_n is None:
				q.append(None)
				print()

			else:
				self.level_order.append(head_n.data)
				print(head_n.data, end=" ")

				if head_n.left is not None:
					q.append(head_n.left)
				if head_n.right is not None:
					q.append(head_n.right)


	def verticalOrder(self):
		if self.root:
			print("-"*50)
			print("Vertical Order Traversal")
			self._verticalOrder()

	def _verticalOrder(self):

		def update_vo(node):
			if node.hd in self.vertical_order:
				self.vertical_order[node.hd].append(node.data)
			else:
				self.vertical_order[node.hd] = [node.data]

		q = []
		q.append(self.root)

		while len(q) > 0:

			head_n = q.pop(0)

			if head_n.left is not None:
				q.append(head_n.left)

				head_n.left.hd = head_n.hd - 1
				update_vo(head_n.left)

			if head_n.right is not None:
				q.append(head_n.right)

				head_n.right.hd = head_n.hd + 1
				update_vo(head_n.right)

		if self.vertical_order:
			for hd in sorted(self.vertical_order):
				print("{} --> {}".format(hd, self.vertical_order[hd]))

	def topView(self):
		if self.root:
			print("-"*50)
			print("Top View")
			self._topView()
			print()

	def _topView(self):
		if self.level_order is None:
			self.levelOrder()
		if self.vertical_order is None:
			self.verticalOrder()

		for hd in sorted(self.vertical_order):
			if len(self.vertical_order[hd]) > 1:
				for node in self.level_order:
					if node in self.vertical_order[hd]:
						print(node, end=" ")
						break
			else:
				print(self.vertical_order[hd][0], end=" ")

	def leftView(self):
		if self.root:
			print("-"*50)
			print("Left View")
			self._leftView()
			print()

	def _leftView(self):
		if self.level_order is None:
			self.levelOrder()
		if self.vertical_order is None:
			self.verticalOrder()

		for hd in range(min(self.vertical_order), 1):
			if len(self.vertical_order[hd]) > 1:
				for node in self.level_order:
					if node in self.vertical_order[hd]:
						print(node, end=" ")
						break
			else:
				print(self.vertical_order[hd][0], end=" ")

	def rightView(self):
		if self.root:
			print("-"*50)
			print("Right View")
			self._rightView()
			print()

	def _rightView(self):
		if self.vertical_order is None:
			self.verticalOrder()
		if self.level_order is None:
			self.levelOrder()

		for hd in range(0, max(self.vertical_order)):
			if len(self.vertical_order[hd]) > 1:
				for node in self.level_order:
					if node in self.vertical_order[hd]:
						print(node, end=" ")
						break
			else:
				print(self.vertical_order[hd][0], end=" ")


	def search(self, key):
		if self.root:
			print("-"*50)
			print("Search {} Node :".format(key), end=" ")
			if self._searchNode(self.root, key):
				print("Found !")
			else:
				print("Not Found !")

	def _searchNode(self, curr_node, key):
		if key == curr_node.data:
			return True
		elif key > curr_node.data and curr_node.right is not None:
			return self._searchNode(curr_node.right, key)
		elif key < curr_node.data and curr_node.left is not None:
			return self._searchNode(curr_node.left, key)
		else:
			return False

	def find(self, key):
		return self._findNode(self.root, key)

	def _findNode(self, curr_node, key):
		if key == curr_node.data:
			return curr_node
		elif key > curr_node.data and curr_node.right is not None:
			return self._findNode(curr_node.right, key)
		elif key < curr_node.data and curr_node.left is not None:
			return self._findNode(curr_node.left, key)
		else:
			return None

	def delete(self, key):
		if self.root:
			print("-"*50)
			print("Delete {} Node ".format(key))
			node = self.find(key)
			if node is not None:
				self._deleteNode(node)
			else:
				print("{} Node does not exists ....".format(key))
			self._getRoot()
			self._inOrder(self.root)
			print()

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
				else:
					parent_n.right = child_n
			else:
				self.root = child_n

		if n_child == 2:
			nxtInOrder_n = getInOrderSucc(node)
			node.data = nxtInOrder_n.data
			self._deleteNode(nxtInOrder_n)

	def height(self):
		if self.root:
			print("-"*50)
			print("Height : {}".format(self._height(self.root, 0)))

	def _height(self, curr_node, curr_height):
		if curr_node is None:
			return curr_height

		left_height = self._height(curr_node.left, curr_height +1 )
		right_height = self._height(curr_node.right, curr_height +1 )

		return max(left_height, right_height)

	def validate(self):
		print("-"*50)
		print("Validate : ", end=" ")
		if self.root:
			max_v, min_v = sys.maxsize, -sys.maxsize
			print(self._validateBST(self.root, min_v, max_v))
		else:
			print("True")
			print("Tree is Empty !")

	def _validateBST(self, curr_node, min_v, max_v):
		if curr_node is None:
			return True

		if (
			curr_node.data > min_v and
			curr_node.data < max_v and
			self._validateBST(curr_node.left, min_v, curr_node.data) and
			self._validateBST(curr_node.right, curr_node.data, max_v)
		):
			return True
		else:
			return False

	def lca(self, p, q):
		if self.root:
			print("-"*50)
			print("LCA of Nodes {} {} : {}".format(p, q, self._lca(self.root, p, q).data))

	def _lca(self, curr_node, p, q):
		if curr_node is None:
			return None

		if curr_node.data == p or curr_node.data == q:
			return curr_node

		left = self._lca(curr_node.left, p, q)
		right = self._lca(curr_node.right, p, q)

		if left is not None and right is not None:
			return curr_node
		else:
			if left is not None:
				return left
			else:
				return right

if __name__ == "__main__":

	in_data = [50, 30, 70, 20, 40, 60, 80, 90]

	t = BSTree()

	t.buildTree(in_data)

	t.getRoot()

	t.height()

	t.validate()

	t.inOrder()
	t.preOrder()
	t.postOrder()

	t.levelOrder()
	t.verticalOrder()

	t.topView()
	t.leftView()
	t.rightView()

	t.search(90)
	t.search(50)
	t.search(30)
	t.search(1000)

	t.lca(60, 70)
	t.lca(20, 90)
	t.lca(50, 90)

	t.delete(90)
	t.delete(40)
	t.delete(30)
	t.delete(50)

	print("-"*50)


"""

OUTPUT : 

--------------------------------------------------
Root : 50
--------------------------------------------------
Height : 4
--------------------------------------------------
Validate :  True
--------------------------------------------------
InOrder Traversal
20 30 40 50 60 70 80 90 
--------------------------------------------------
PreOrder Traversal
50 30 20 40 70 60 80 90 
--------------------------------------------------
PostOrder Traversal
20 40 30 60 90 80 70 50 
--------------------------------------------------
Level Order Traversal
50 
30 70 
20 40 60 80 
90 
--------------------------------------------------
Vertical Order Traversal
-2 --> [20]
-1 --> [30]
0 --> [40, 60]
1 --> [70]
2 --> [80]
3 --> [90]
--------------------------------------------------
Top View
20 30 40 70 80 90 
--------------------------------------------------
Left View
20 30 40 
--------------------------------------------------
Right View
40 70 80 
--------------------------------------------------
Search 90 Node : Found !
--------------------------------------------------
Search 50 Node : Found !
--------------------------------------------------
Search 30 Node : Found !
--------------------------------------------------
Search 1000 Node : Not Found !
--------------------------------------------------
LCA of Nodes 60 70 : 70
--------------------------------------------------
LCA of Nodes 20 90 : 50
--------------------------------------------------
LCA of Nodes 50 90 : 50
--------------------------------------------------
Delete 90 Node 
Root : 50
20 30 40 50 60 70 80 
--------------------------------------------------
Delete 40 Node 
Root : 50
20 30 50 60 70 80 
--------------------------------------------------
Delete 30 Node 
Root : 50
20 50 60 70 80 
--------------------------------------------------
Delete 50 Node 
Root : 60
20 60 70 80 
--------------------------------------------------
"""



