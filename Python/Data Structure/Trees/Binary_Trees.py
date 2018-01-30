# -----------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
"""
Binary Trees is an ordered tree with the following properties :
  1. Every node has at the most two children 
  2. Each child node is labeled as being either a ;eft child or a right child 
  3. A left child precedes a right child in the order of children of a node

  The subtree rooted at a left or right child of an internel node v is called left subtree or right subtree, 
  respectively, of v. A binary tree is proper if each node has either zero or twp children. Thus, in a proper
  binary tree, every internal node has exactly two children. 

A Recursive Binary Tree Defination 
  * A node r, called root of T, that stores an element 
  * A binary tree (possibly empty), called the left subtree of T
  * A binary tree (possible empty), called the right subtree of T 
"""
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
class BinaryTree(Tree):
	""" Abstract base class representing a binary tree structure """

	#--------------------------------------------------------------------------------------------------------------
	# Additional abstract methods 
	def left(self, p):
		""" Return a Position representing p's left child 

		    Return None if p dpes not have a left child 
		"""
		raise NotImplementedError('must be implemented by subclass')

	def right(self, p):
		""" Return Position representing p's right child 

		Return None of p does not have a right child 
		"""
		raise NotImplementedError('must be implemented by subclass')

  #---------------------------------------------------------------------------------------------------------------
  # Concrete methods implemented in class 
  def sibling(self, p):
    """ Return a Position representing p's sibling (or None if no sibling) """
    parent = self.parent(p)
    if parent is None:
    	return None
    else:
    	if p == self.left(parent):
    		return self.right(parent)
    	else:
    		return self.left(parent)


  def children(self, p):
    """ Generate an iteration of Positions representing p's children """
    if self.left(p) is not None:
    	yield self.left(p)
    if self.right(p) is not None:
    	yield self.right(p)
    		
    	

