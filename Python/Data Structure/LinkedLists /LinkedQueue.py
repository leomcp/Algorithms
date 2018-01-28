class LinkedQueue:
	""" FIFO queue implementation using a sigle linked list for storage """
    #--------------------------------------------------------------------------------
	class _Node:
		""" LightWeight, non public class for storing a singly linked node """
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element 
			self._next = next 
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	def __init__(self):
		""" Create an empty queue """
		self._head = None
		self._tail = None 
		self._size = 0 
	#--------------------------------------------------------------------------------
	def __len__(self):
		""" Return the number of element in the queue """
		return self._size
	#--------------------------------------------------------------------------------
	def is_empty(self):
		""" Return True if the queue id empty """
		return self._size == 0 
	#--------------------------------------------------------------------------------
	def first(self):
		""" Return (but not remove) the e,ement at the front of the queue """
		if self.is_empty():
			raise Empty('Queue is empty ')
		return self._head._element
	#--------------------------------------------------------------------------------
	def dequeue(self):
		""" Remove and return the first element of the queueu (FIFO)

		raise Empty exception if the queueu is empty 
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._head._element
		self._head = self._head._next 
		self._size -= 1 
		if self.is_empty():
			self._tail = None
		return answer 
	#--------------------------------------------------------------------------------
	def enqueue(self, e):
		""" Add element to the back of queue """
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest 
		else:
			self._tail._next = newest 
		self._tail = newest 
		self._size +=1 
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

if __name__ == '__main__':

	l = LinkedQueue()

	s1 = l.__len__()
	print('Initial size : ', s1)

	l.enqueue(10)
	l.enqueue(20)
	l.enqueue(30)
	l.enqueue(40)
	l.enqueue(50)
	l.enqueue(60)

	s2 = l.__len__()
	print('Size : ', s2)

	f = l.first()
	print('First element : ', f)

	d = l.dequeue()
	print('Dequeue element : ', d)

	s3 = l.__len__()
	print('Size : ', s3)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""
OUTPUT :
Initial size :  0
Size :  6
First element :  10
Dequeue element :  10
Size :  5

"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


