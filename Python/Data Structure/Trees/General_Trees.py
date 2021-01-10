# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
class Tree:
	""" Abstract base class representing a tree structure """
	# Nested Position class 
	# -------------------------------------------------------------------------------------------------------------
	class Postion:

		""" An abstract representing the location of a single element """

		def element(self):
			""" Return the element stored at this position """
			raise NotImplementedError('must be implemented by subclass')

		def __eq__(self, other):
			""" Return True if other Position represents the same location """
			raise NotImplementedError('must implemented by subclass')

		def __ne__(self, other):
			""" Return True if other does not represent the same location """
			return not(self == other)

	# Abstract methods that concrete subclass must support
	# -------------------------------------------------------------------------------------------------------------
	def root(self):
		""" Return Position representing the tree's root (or None if empty) """
		raise NotImplementedError('must be implemented by subclass')

	def parent(self, p):
		""" Return Position representing p's parent (or None if p is root) """
		raise NotImplementedError('must be implemented by subclass')

	def num_children(self, p):
		""" Return the number of children that position p has """
		raise NotImplementedError('must be inplemented by subclass')

	def children(self, p):
		""" Generate an iteration of Positions p's children """
		raise NotImplementedError('must be implemented by subclass')

	def __len__(self):
		""" Return the total number of elements in tree """
		raise NotImplementedError('must be implemented by subclass')

	# Concrete methods implemented in this class
	# -------------------------------------------------------------------------------------------------------------
	def is_root(self, p):
		""" Return True if Position p represents the root of the tree """
		return self.root == p

	def is_leaf(self, p):
		""" Return True of position o does not have any children """
		return self.num_children(p) == 0

	def is_empty(self):
		""" Return True if the tree is empty """
		return len(self) == 0

	def depth(self, p):
		""" Rrturn the number of levels separating Position p from the root """
		"""
		Let p be the position of a node of a tree T. The depth p is the number of ancestors of p,
		excluding p itself, The defination implies that depth of root of T is 0. The depth of p can
		also be recursively defined as follows :
		 * If p is the root, then depth of p is 0
		 * Otherwise, the depth of p is one plus the depth of the parent p
		"""
		if self.is_root(p):
			return 0
		else:
			return 1 + self.depth(self.parent(p))

	""" Height """
	""" Height of a position p in a tree T is also defined recursively :
	    * If p is a leaf, then the height of p is 0
	    * Otherwise, the height of p is more than the maximum of height's of p's children
	    The height of a non-empty tree T is the height of the root of T.

	    Preposition : The height of a non empty tree T is equal to the maximum of the depths of its leaf 
	                  positions.
	 """

    def _height1(self):
    	""" Return the height of the tree """
    	return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    """ Computing height of the tree efficiently, in O(n) wprst-case time, by relying instead on the original
    recursive function. We will paramaterized a function beased on a position within tree, and calculate the 
    height of the subtree rooted at that position. 
    """

    def _height2(self, p):
    	""" Return the height of the subtree rooted at Position p """
    	if self.is_leaf(p):
    		return 0
    	else:
    		return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
    	""" Return the height of the subtree rooted at Position p.

    	If p is None, return the height of the entire tree
    	"""
    	if p is None:
    		p = self.root()
    	return self._height2(p)  # start _height2 recursion
	# -------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------