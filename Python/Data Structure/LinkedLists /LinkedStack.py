#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class LinkedStack:
	""" LIFO Stack implementation using a single linked list for storage """
	#---------------------------------------------------------------------------
	class _Node:
		""" LightWeight, non public class for storing a singly linked node """
		__slots__ = '_element', '_next'  # steamline memory usage 

		def __init__(self, element, next):
			self._element  = element
			self._next = next  
	#---------------------------------------------------------------------------
	def __init__(self):
		self._head = None 
		self._size = 0 
	#---------------------------------------------------------------------------
	def __len__(self):
		return self._size
	#---------------------------------------------------------------------------
	def is_empty(self):
		return self._size == 0
	#---------------------------------------------------------------------------
	def push(self,  e):
		""" Add element e to the top of stack """
		self._head = self._Node(e, self._head)
		self._size += 1
	#---------------------------------------------------------------------------
	def top(self):
		""" Return (but do not remove) the element at the top of the stack 

		Raise Empty exception if the stack is empty 
		"""
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element 
	#---------------------------------------------------------------------------
	def pop(self):
		""" Remove and return element from the top of the stack 

		Raise Empty Exception if the stack is empty
		"""
		if self.is_empty():
			raise Empty('Stack is empty')
		answer = self._head._element
		self._head = self._head._next 
		self._size -= 1
		return answer 
	#---------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

if __name__ == '__main__':

	linkedStack = LinkedStack()

	linkedStack.push(10)
	linkedStack.push(20)
	linkedStack.push(30)
	linkedStack.push(40)

	top = linkedStack.top()
	print('Top element : ', top)

	pop = linkedStack.pop()
	print('Poped element : ', pop)

	size =  linkedStack.__len__()
	print('Length of the linkedlist : ', size )

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
"""
OUTPUT :
Top element :  40
Poped element :  40
Length of the linkedlist :  3
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------







    

