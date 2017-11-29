import sys 

class Node:
	def __init__(self, value=None):
		self.value = value
		self.left_child = None
		self.right_child = None

def validator_bst(root, min=-sys.maxint, max= sys.maxint):
	if root ==None:
		return True
	if (root.value>min and root.value<max and validator_bst(root.left_child,min,root.value) and validator_bst(root.right_child,root.value,max)):
		return True
	else:
		return False 

# Test case 
root = Node(5)
l=Node(4)
r=Node(6)

root.left_child=l
root.right_child=r

print validator_bst(root)


