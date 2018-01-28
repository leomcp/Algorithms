class _DoublyLinkedListBase:
	""" A base class providing a doubly linked list representation """
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
	class _Node:
		""" Lightweight, non public class for storing a doubly linked list """
		__slots__ = '_element', '_prev', '_next'

		def __init__(self, elemnt, prev, next):
			self._element = element 
			self._prev = prev 
			self._next = next 
	#--------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------------
	def __init__(self):
		""" Create an empty list """
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0 
	#--------------------------------------------------------------------------------------
	def __len__(self):
		return self.size 
	#--------------------------------------------------------------------------------------
	def is_empty(self):
		""" Return True if list is empty """
		return self._size == 0 
	#--------------------------------------------------------------------------------------
	def _insert_between(self, e, predecessor, successor):
		""" Add element e between two existing nodes and return new node """
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1 
		return newest
	#--------------------------------------------------------------------------------------
	def _delete_node(self, node):
		""" Delete nonsentinel node from the list and return element """
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element
		node._prev = node._next = node.element = None
		return element 
	#--------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class LinkedDeque(_DoublyLinkedListBase):
	""" Double-ended queue implementation based on doubly linked list """
    #--------------------------------------------------------------------------------------
	def first(self):
		""" Return (but do not remove) the element at the front of the deque """
		if self.is_empty():
			raise Empty('Deqque is empty')
		return self._header._next._element 
	#--------------------------------------------------------------------------------------

