
class Node:
	def __init__(self, data):
		self.data = data 
		self.right = None
		self.left = None
		self.hd = 0 

class BSTree:
	def __init__(self):
		self.root  = None 
		self.height = 0 

		self.lvl_order = []
		self.vrt_map = {}
		self.top_order = []

	def get_root(self):
		""" Returns root of the Binary Search Tree """
		if self.root:
			return self.root.data

	def insert(self, elem):
		""" Inserts new element in Binary Search Tree"""
		if self.root is None:
			self.root = Node(elem)
		else:
			self._insert(self.root, elem)
			print("{} is inserted .....".format(elem))

	def _insert(self, curr_node, elem):
		if curr_node.data > elem:
			if curr_node.left is None:
				curr_node.left = Node(elem)
			else:
				self._insert(curr_node.left, elem)
		elif curr_node.data < elem:
			if curr_node.right is None:
				curr_node.right = Node(elem)
			else:
				self._insert(curr_node.right, elem)
		else:
			print("Already inserted {}".format(elem))

	def inorder_traversal(self):

		if self.root:
			print("-"*30)
			print("Inorder Traversal")
			print("-"*30)
			self._inorder_recursive(self.root)
			print()
			self._inorder_iterative()
			print()

	def _inorder_recursive(self, curr_node):
		if curr_node:
			self._inorder_recursive(curr_node.left)
			print(curr_node.data, end=" ")
			self._inorder_recursive(curr_node.right)


	def _inorder_iterative(self):
		inorder_list = []
		s = []

		curr_node = self.root 

		while True:

			if curr_node is not None:
				s.append(curr_node)
				curr_node = curr_node.left 

			elif s :
				curr_node = s[-1]
				del(s[-1])
				inorder_list.append(curr_node.data)
				curr_node = curr_node.right

			else:
				break

		if inorder_list:
			for elem in inorder_list:
				print(elem, end=" ")


	def preorder_traversal(self):
		if self.root:
			print("-"*30)
			print("Preorder Traversal")
			print("-"*30)
			self._preorder_recursive(self.root)
			print()
			self._preorder_iterative()

	def _preorder_recursive(self, curr_node):
		if curr_node:
			print(curr_node.data, end=" ")
			self._preorder_recursive(curr_node.left)
			self._preorder_recursive(curr_node.right)

	def _preorder_iterative(self):
		if self.root:
			preorder_list = []

			s = []
			s.append(self.root)

			while len(s)>0:
				pop_node = s[-1]
				del(s[-1])
				if pop_node.right is not None:
					s.append(pop_node.right)
				if pop_node.left is not None:
					s.append(pop_node.left)
				preorder_list.append(pop_node.data)

			if preorder_list:
				for elem in preorder_list:
					print(elem, end=" ")
				print()

	def postorder_traversal(self):
		if self.root:
			print("-"*30)
			print("Postorder Traversal")
			print("-"*30)
			self._postorder_recursive(self.root)
			print()
			self._postorder_iterative()

	def _postorder_recursive(self, curr_node):
		if curr_node:
			self._postorder_recursive(curr_node.left)
			self._postorder_recursive(curr_node.right)
			print(curr_node.data, end=" ")

	def _postorder_iterative(self):
		if self.root:
			s_1 = []
			s_2 = []

			s_1.append(self.root)

			while len(s_1)>0:
				pop_node = s_1[-1]
				del(s_1[-1])

				if pop_node.left is not None:
					s_1.append(pop_node.left)
				if pop_node.right is not None:
					s_1.append(pop_node.right)

				s_2.append(pop_node.data)

			if s_2:
				for idx in range(len(s_2)-1, -1, -1):
					print(s_2[idx], end=" ")
				print()

	def levelorder_traversal(self):
		if self.root:

			print("-"*30)
			print("Level Order Traversal")
			print("-"*30)

			q = []

			q.append(self.root)
			q.append(Node(None))

			while len(q)>1:
				head = q[0]
				del(q[0])

				if head.data is None:
					q.append(Node(None))
					print()
				else:
					print(head.data, end=" ")
					self.lvl_order.append(head.data)

				if head.left is not None:
					q.append(head.left)
				if head.right is not None:
					q.append(head.right)
			print()

	def verticalorder_traversal(self):
		if self.root:
			print("-"*30)
			print("Vertical Order Traversal")
			print("-"*30)
			q = []

			q.append(self.root)
			self.root.hd = 0 
			self.vrt_map[0] = [self.root]


			while len(q) > 0:
				curr_node = q[0]
				del(q[0])

				if curr_node.left is not None:
					q.append(curr_node.left)
					curr_node.left.hd = curr_node.hd - 1

					if curr_node.left.hd in list(self.vrt_map.keys()):
						self.vrt_map[curr_node.left.hd].append(curr_node.left)
					else:
						self.vrt_map[curr_node.left.hd] = [curr_node.left]
					
				if curr_node.right is not None:
					q.append(curr_node.right)
					curr_node.right.hd = curr_node.hd + 1 

					if curr_node.right.hd in list(self.vrt_map.keys()):
						self.vrt_map[curr_node.right.hd].append(curr_node.right)
					else:
						self.vrt_map[curr_node.right.hd] = [curr_node.right]

			if self.vrt_map:
				for key in sorted(list(self.vrt_map.keys())):
					for elem in self.vrt_map[key]:
						print(elem.data, end=" ")
					print()


	def toporder_traversal(self):
		if self.root:
			print("-"*30)
			print("Top Order Traversal")
			print("-"*30)

			if self.lvl_order is None:
				self.levelorder_traversal()
			if self.vrt_map is None:
				self.verticalorder_traversal()

			for hd in sorted(list(self.vrt_map.keys())):
				if len(self.vrt_map[hd])> 1:
					for elem in self.lvl_order:
						if elem in self.vrt_map[hd]:
							self.top_order.append(elem)
							break
				else:
					self.top_order.append(self.vrt_map[hd][0])

			if self.top_order:
				for curr_node in self.top_order:
					print(curr_node.data, end=" ")
				print()

	def spiral_order_traversal(self):
		pass


if __name__ == "__main__":
	bst = BSTree()

	in_data = [10, 5, 15, 3, 7, 12, 18]

	for elem in in_data:
		bst.insert(elem)

	print()


	bst.inorder_traversal()
	bst.preorder_traversal()
	bst.postorder_traversal()
	bst.levelorder_traversal()
	bst.verticalorder_traversal()
	bst.toporder_traversal()
	bst.spiral_order_traversal()


"""
OUTPUT :

5 is inserted .....
15 is inserted .....
3 is inserted .....
7 is inserted .....
12 is inserted .....
18 is inserted .....

------------------------------
Inorder Traversal
------------------------------
3 5 7 10 12 15 18 
3 5 7 10 12 15 18 
------------------------------
Preorder Traversal
------------------------------
10 5 3 7 15 12 18 
10 5 3 7 15 12 18 
------------------------------
Postorder Traversal
------------------------------
3 7 5 12 18 15 10 
3 7 5 12 18 15 10 
------------------------------
Level Order Traversal
------------------------------
10 
5 15 
3 7 12 18 
------------------------------
Vertical Order Traversal
------------------------------
3 
5 
10 7 12 
15 
18 
------------------------------
Top Order Traversal
------------------------------
3 5 15 18 

"""


