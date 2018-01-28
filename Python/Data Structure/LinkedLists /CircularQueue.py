class CircularQueue:
	""" Queue implementation using circularly linked list for storage """
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
	class _Node:
		""" LightWwight, non public class for storing a singly linked list node """

		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next 
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
	def __init__(self):
		""" Create an empty Queue """

		self._tail = None
		self._size = 0 
    #-------------------------------------------------------------------------------------
	def __len__(self):
		""" Return the number of element inn the queue """
		return self._size 
    #-------------------------------------------------------------------------------------
	def is_empty(self):
		""" Return Ture if the queue is empty """
		return self._size == 0
	#-------------------------------------------------------------------------------------
	def first(self):
		""" Return (but do not remove ) the element at the front og the queue 

		Raise Empty exception if the queueu is empty 
		"""

		if self.is_empty():
			raise Empty('Queue is Empty')
		head = self._tail._next 
		return head._element 
	#-------------------------------------------------------------------------------------
	def dequeue(self):
		""" Remove and return first element of the queue 

		Raise Empty exception if the queue is empty 
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		oldhead = self._tail._next 
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = oldhead._next 
		self._size -= 1
		return oldhead._element
	#-------------------------------------------------------------------------------------
	def enqueue(self, e):
		""" Add element to the back of queue """
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest # initialy circular 
		else:
			newest._next = self._tail._next 
			self._tail._next = newest 
		self._tail =  newest
		self._size += 1
	#-------------------------------------------------------------------------------------
	def rotate(self):
		""" Rotate front element to the back of the queue """
		if self._size > 0:
			self._tail = self._tail._next 
	#-------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
if __name__ == '__main__':

	cq = CircularQueue()

	s1 = cq.__len__()
	print('Initial Size : ', s1)

	cq.enqueue(10)
	cq.enqueue(20)
	cq.enqueue(30)
	cq.enqueue(40)
	cq.enqueue(50)
	cq.enqueue(60)

	s2 = cq.__len__()
	print('Size : ', s2)

	f1 = cq.first()
	print('First element : ', f1)

	d1 = cq.dequeue()
	print('Dequeued element : ', d1)

	s3 = cq.__len__()
	print('Size : ', s3)

	cq.rotate()

	f2 = cq.first()
	print('First element : ', f2)
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
"""
OUTPUT : 
Initial Size :  0
Size :  6
First element :  10
Dequeued element :  10
Size :  5
First element :  30
"""
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------




