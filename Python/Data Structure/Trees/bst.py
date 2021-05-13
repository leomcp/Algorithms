
from __future__ import print_function
import sys 

class Node:

	def __init__(self, data):
		self.data = data

		self.left = None
		self.right = None
		self.parent = None
		self.next = None
		self.prev = None

		self.hd = 0

class BSTree:

	def __init__(self):
		self.root = None

		self.level_order = {}
		self.vertical_order = {}

	def build(self, in_data):
		print("-"*30)
		print("Building Tree : ", end="")
		for key in in_data:
			self.insert(key)
		if self.root:
			print("Complete !")
			print("{} Nodes inserted".format(len(in_data)))
			print("Root : {}".format(self.root.data))

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
			print("{} Node already inserted ....".format(key))

	def validate(self):
		print("-"*30)
		print("Is Tree Valid BST ? : ", end="")
		if self.root:
			min_v, max_v = -sys.maxsize, sys.maxsize
			if self._validateBST(self.root, min_v, max_v):
				print("Valid !")
			else:
				print("InValid !")

	def _validateBST(self, curr_node, min_v, max_v):
		if curr_node is None:
			return True
		if(
			curr_node.data > min_v and
			curr_node.data < max_v and
			self._validateBST(curr_node.left, min_v, curr_node.data) and
			self._validateBST(curr_node.right, curr_node.data, max_v)
		):
			return True
		else:
			return False

	def min(self):
		print("-"*30)
		print("Min : ", end="")
		if self.root:
			print(self._getMin(self.root))

	def _getMin(self, curr_node):
		while curr_node.left is not None:
			curr_node = curr_node.left
		return curr_node.data

	def max(self):
		print("-"*30)
		print("Max : ", end="")
		if self.root:
			print(self._getMax(self.root))

	def _getMax(self, curr_node):
		while curr_node.right is not None:
			curr_node = curr_node.right
		return curr_node.data

	def height(self):
		print("-"*30)
		print("Height : ", end="")
		if self.root:
			print(self._height(self.root, 0))

	def _height(self, curr_node, curr_height):
		if curr_node is None:
			return curr_height
		left = self._height(curr_node.left, curr_height + 1)
		right = self._height(curr_node.right, curr_height + 1)
		return max(left, right)

	def inOrder(self):
		print("-"*30)
		print("InOrder Traversal : ")
		if self.root:
			self._inOrder(self.root)
			print()

	def _inOrder(self, curr_node):
		if curr_node:
			self._inOrder(curr_node.left)
			print(curr_node.data, end=" ")
			self._inOrder(curr_node.right)

	def preOrder(self):
		print("-"*30)
		print("PreOrder Traversal : ")
		if self.root:
			self._preOrder(self.root)
			print()

	def _preOrder(self, curr_node):
		if curr_node:
			print(curr_node.data, end=" ")
			self._preOrder(curr_node.left)
			self._preOrder(curr_node.right)

	def postOrder(self):
		print("-"*30)
		print("PostOrder Traversal : ")
		if self.root:
			self._postOrder(self.root)
			print()

	def _postOrder(self, curr_node):
		if curr_node:
			self._postOrder(curr_node.left)
			self._preOrder(curr_node.right)
			print(curr_node.data, end=" ")

	def levelOrder(self):
		print("-"*30)
		print("LevelOrder Traversal : ")
		if self.root:
			self._levelOrder()

	def _levelOrder(self):
		q = []
		q.append(self.root)

		lvl = 0

		while len(q) > 0:
			currlvl = []
			for _ in range(len(q)):
				head_n = q.pop(0)
				currlvl.append(head_n.data)

				if head_n.left is not None:
					q.append(head_n.left)
				if head_n.right is not None:
					q.append(head_n.right)

			self.level_order[lvl] = currlvl
			lvl += 1

		if self.level_order:
			for lvl in sorted(self.level_order):
				print("{} --> {}".format(lvl, self.level_order[lvl]))

	def verticalOrder(self):
		print("-"*30)
		print("VerticalOrder Traversal : ")
		if self.root:
			self._verticalOrder()

	def _verticalOrder(self):

		def update(node):
			if node.hd in self.vertical_order:
				self.vertical_order[node.hd].append(node.data)
			else:
				self.vertical_order[node.hd] = [node.data]

		q = []
		q.append(self.root)

		self.root.hd = 0
		update(self.root)

		while len(q) > 0:
			head_n = q.pop(0)

			if head_n.left is not None:
				q.append(head_n.left)
				head_n.left.hd = head_n.hd - 1
				update(head_n.left)

			if head_n.right is not None:
				q.append(head_n.right)
				head_n.right.hd = head_n.hd + 1
				update(head_n.right)

		if self.vertical_order:
			for hd in sorted(self.vertical_order):
				print("{} --> {}".format(hd, self.vertical_order[hd]))

	def populateNext(self):

		def displayNextLvlWise():
			q = []
			q.append(self.root)
			while len(q) > 0:
				head_n = q.pop(0)
				head_n.next = self._getInOrderSucc(head_n)
				print("{} --> {}".format(head_n.data, head_n.next))

				if head_n.left is not None:
					q.append(head_n.left)
				if head_n.right is not None:
					q.append(head_n.right)

		print("-"*30)
		print("Populate Next : ")
		if self.root:
			displayNextLvlWise()

	def _getInOrderSucc(self, node):
		if node.right is not None:
			return self._getMin(node.right)
		else:
			parent_n = node.parent
			while parent_n is not None:
				if parent_n.left == node:
					return parent_n.data
				else:
					node = parent_n
					parent_n = node.parent

	def populatePrev(self):

		def displayPrevLvlWise():
			q = []
			q.append(self.root)

			while len(q) > 0:
				head_n = q.pop(0)
				head_n.prev = self._getInOrderPrev(head_n)
				print("{} <-- {}".format(head_n.data, head_n.prev))

				if head_n.left is not None:
					q.append(head_n.left)
				if head_n.right is not None:
					q.append(head_n.right)

		print("-"*30)
		print("Populate Prev : ")
		if self.root:
			displayPrevLvlWise()

	def _getInOrderPrev(self, node):
		if node.left is not None:
			return self._getMax(node.left)
		else:
			parent_n = node.parent
			while parent_n is not None:
				if parent_n.right == node:
					return parent_n.data
				else:
					node = parent_n
					parent_n = parent_n.parent


	def lca(self, p, q):
		print("-"*30)
		print("LCA Of {} {} Nodes : ".format(p, q), end="")
		if self.root:
			print(self._lca(self.root, p, q).data)

	def _lca(self, curr_node, p, q):
		if curr_node is None:
			return None

		if curr_node.data == p or curr_node.data == q:
			return curr_node

		left = self._lca(curr_node.left, p, q)
		right = self._lca(curr_node.right, p, q)

		if left is not None and right is not None:
			return curr_node
		elif left is not None:
			return left
		else:
			return right

	def search(self, key):
		print("-"*30)
		print("Search Node {} : ".format(key), end="")
		if self.root:
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
			return None

	def delete(self, key):
		print("-"*30)
		print("Delete Node {} : ".format(key))
		if self.root:
			node = self._findNode(self.root, key)
			if node is not None:
				self._deleteNode(node)
			else:
				print(" {} Node does not exists....".format(key))
			if self.root:
				print("InOrder Traversal : ", end="")
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
		print(" N Child : {}".format(n_child), end=" ")
		parent_n = node.parent

		if n_child == 0:
			if parent_n is not None:
				print(" Attach : {} --> None".format(parent_n.data))
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
				print(" Attach : {} --> {}".format(parent_n.data, child_n.data))
				if parent_n.left == node:
					parent_n.left = child_n
					child_n.parent = parent_n
				else:
					parent_n.right = child_n
					child_n.parent = parent_n
			else:
				self.root = child_n
				self.root.parent = None

		if n_child == 2:
			next_n = getInOrderSucc(node)
			print(" InOrder Succ Node : {} (Replace {} == {})".format(next_n.data, node.data, next_n.data))
			node.data = next_n.data
			print(" Delete Node {} : ".format(next_n.data))
			self._deleteNode(next_n)


if __name__ == "__main__":

	in_data = [50, 30, 70, 20, 40, 60, 80, 35, 45, 65, 90]

	t = BSTree()

	t.build(in_data)

	t.validate()

	t.min()
	t.max()

	t.height()

	t.inOrder()
	t.preOrder()
	t.postOrder()

	t.levelOrder()
	t.verticalOrder()

	t.populateNext()
	t.populatePrev()

	t.lca(80, 90)
	t.lca(20, 90)
	t.lca(50, 90)

	t.search(100)
	t.search(50)
	t.search(80)
	t.search(20)
	t.search(30)

	t.delete(100) # NA
	t.delete(80) # 1 Child 
	t.delete(90) # 0 Child
	t.delete(30) # 2 Child
	t.delete(50) # Root Node

	print("-"*30)


"""
BST : 

				50
	30 					   70
	
20 		40				60		80

	35		45				65		90


------------------------------
Building Tree : Complete !
11 Nodes inserted
Root : 50
------------------------------
Is Tree Valid BST ? : Valid !
------------------------------
Min : 20
------------------------------
Max : 90
------------------------------
Height : 4
------------------------------
InOrder Traversal : 
20 30 35 40 45 50 60 65 70 80 90 
------------------------------
PreOrder Traversal : 
50 30 20 40 35 45 70 60 65 80 90 
------------------------------
PostOrder Traversal : 
20 40 35 45 30 70 60 65 80 90 50 
------------------------------
LevelOrder Traversal : 
0 --> [50]
1 --> [30, 70]
2 --> [20, 40, 60, 80]
3 --> [35, 45, 65, 90]
------------------------------
VerticalOrder Traversal : 
-2 --> [20]
-1 --> [30, 35]
0 --> [50, 40, 60]
1 --> [70, 45, 65]
2 --> [80]
3 --> [90]
------------------------------
Populate Next : 
50 --> 60
30 --> 35
70 --> 80
20 --> 30
40 --> 45
60 --> 65
80 --> 90
35 --> 40
45 --> 50
65 --> 70
90 --> None
------------------------------
Populate Prev : 
50 <-- 45
30 <-- 20
70 <-- 65
20 <-- None
40 <-- 35
60 <-- 50
80 <-- 70
35 <-- 30
45 <-- 40
65 <-- 60
90 <-- 80
------------------------------
LCA Of 80 90 Nodes : 80
------------------------------
LCA Of 20 90 Nodes : 50
------------------------------
LCA Of 50 90 Nodes : 50
------------------------------
Search Node 100 : Not Found !
------------------------------
Search Node 50 : Found !
------------------------------
Search Node 80 : Found !
------------------------------
Search Node 20 : Found !
------------------------------
Search Node 30 : Found !
------------------------------
Delete Node 100 : 
 100 Node does not exists....
InOrder Traversal : 20 30 35 40 45 50 60 65 70 80 90 
Root : 50
Height : 4
------------------------------
Delete Node 80 : 
 N Child : 1  Attach : 70 --> 90
InOrder Traversal : 20 30 35 40 45 50 60 65 70 90 
Root : 50
Height : 4
------------------------------
Delete Node 90 : 
 N Child : 0  Attach : 70 --> None
InOrder Traversal : 20 30 35 40 45 50 60 65 70 
Root : 50
Height : 4
------------------------------
Delete Node 30 : 
 N Child : 2  InOrder Succ Node : 35 (Replace 30 == 35)
 Delete Node 35 : 
 N Child : 0  Attach : 40 --> None
InOrder Traversal : 20 35 40 45 50 60 65 70 
Root : 50
Height : 4
------------------------------
Delete Node 50 : 
 N Child : 2  InOrder Succ Node : 60 (Replace 50 == 60)
 Delete Node 60 : 
 N Child : 1  Attach : 70 --> 65
InOrder Traversal : 20 35 40 45 60 65 70 
Root : 60
Height : 4
------------------------------

"""