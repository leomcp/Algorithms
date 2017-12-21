#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
"""
QUEUES :

Queue is a collection of objects that are inserted and removed according to the first-in, 
first-out (FIFO) principle. Elements, can be inserted at any time, but only the element 
that has been in the queue the longest can be next removed.

THE QUEUE ABSTRACT DATA TYPE :
The queue acstract data type (ADT) supports the following two fundamental methods for queue Q :
  
  Q.enqueue(e) : Add element e to the back of queue Q
  Q.dequeue() : Remove and return the first element from queue Q;
                an error occurs if queue is empty
  Queue ADT also supports  following methods :
  Q.first() : Return's True if queue Q does not contain any elements.
  len(Q) : Return number of elements in queue Q; in Python, we implement this with th special 
           method __len__
  Q.is_empty() : Return True if queue Q does not contin any element.
  """
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

class ArrayQueue:
	""" FIFO queue implementation using a Python list as underlying storage """
	DEFAULT_CAPACITY = 10 # moderate capacity for all new queues 

	def __init__(self):
		""" Create an empty queue """

		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def is_empty(self):
		""" Return True if the queue is empty """
		return self._size == 0 

	def __len__(self):
		""" Return the number of element in the queue """
		return self._size 

	def first(self):
		""" Return (but do not remove) the element at the front of the queue.

		Raise Empty exception if the queue is empty
		"""

		if self.is_empty():
			raise Empty('Queue is empty')

		return self._data[self._front]

	def dequeue(self):
		""" Remove and return the first element of the queue 

		Raise an exception if the queue is empty 
		"""

		if self.is_empty():
			raise Empty('Queue is empty')

		answer = self._data[self._front]
		self._data[self._front] = None # garbage collection 
		self._front = (self._front + 1) % len(self._data)
		self._size -=1

		print('Dequeue')
		print('front :',self._front,'\t size : ',self._size,'\t length : ',len(self._data))
		return answer  

	def enqueue(self, e):
		""" Add element to the back of queue """

		if self._size == len(self._data):
			self._resize(2 * len(self._data)) # double the array size 
		avail = (self._front + self._size) % len(self._data)
		print('enqueue')
		print('avail : ',avail,'\t front : ',self._front,'\t size : ',self._size,'\t length : ',len(self._data))

		self._data[avail] = e 
		self._size += 1

	def _resize(self, cap):
		""" resize to a new list of capacity >= len(self) """

		old = self._data
		self._data = [None] * cap
		walk = self._front 
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0

	def print_Queue(self):
		""" Prints the whole queue 

		Raise an exception if queue is empty 
		"""
		print("Queue --> ")
		for i in (10):

			print(self._data[i])

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
""" 
ADDING AND REMOVING ELEMENTS 

The goal of the enqueue method is to add a new element to the back pf the queue. We need to deter
mine the proper index at which to place the new element. We compute the location of the next opening
based on formula :
    avail = (self._front + self._size) % len(self._data)


When dequeue method is called, the current value of self._front designates the index of the value that 
is index of the value that is to be removed and returned. 
   * Keep the local refrence to the element that wull be returned, seting :
     answer = self._data[self._front]
   * just prior to removing the refrence to that object from the list, with the assignment 
     self._data[self._front] = None
Second, responsibility of dequeue method is to update the value of _front to reflect removal of the 
element, and the presumed promotion of the second element to become the new first. 

"""
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
if __name__ == '__main__':

	queue = ArrayQueue()

	for i in range(30):
		queue.enqueue(i)
    
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()

	for j in range(5):
		queue.enqueue(j)

	#queue.print_Queue()

	for k in range(30):
		queue.dequeue()

	queue.enqueue(10)
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
"""
OUTPUT :

enqueue
avail :  0 	 front :  0 	 size :  0 	 length :  10
enqueue
avail :  1 	 front :  0 	 size :  1 	 length :  10
enqueue
avail :  2 	 front :  0 	 size :  2 	 length :  10
enqueue
avail :  3 	 front :  0 	 size :  3 	 length :  10
enqueue
avail :  4 	 front :  0 	 size :  4 	 length :  10
enqueue
avail :  5 	 front :  0 	 size :  5 	 length :  10
enqueue
avail :  6 	 front :  0 	 size :  6 	 length :  10
enqueue
avail :  7 	 front :  0 	 size :  7 	 length :  10
enqueue
avail :  8 	 front :  0 	 size :  8 	 length :  10
enqueue
avail :  9 	 front :  0 	 size :  9 	 length :  10
enqueue
avail :  10 	 front :  0 	 size :  10 	 length :  20
enqueue
avail :  11 	 front :  0 	 size :  11 	 length :  20
enqueue
avail :  12 	 front :  0 	 size :  12 	 length :  20
enqueue
avail :  13 	 front :  0 	 size :  13 	 length :  20
enqueue
avail :  14 	 front :  0 	 size :  14 	 length :  20
enqueue
avail :  15 	 front :  0 	 size :  15 	 length :  20
enqueue
avail :  16 	 front :  0 	 size :  16 	 length :  20
enqueue
avail :  17 	 front :  0 	 size :  17 	 length :  20
enqueue
avail :  18 	 front :  0 	 size :  18 	 length :  20
enqueue
avail :  19 	 front :  0 	 size :  19 	 length :  20
enqueue
avail :  20 	 front :  0 	 size :  20 	 length :  40
enqueue
avail :  21 	 front :  0 	 size :  21 	 length :  40
enqueue
avail :  22 	 front :  0 	 size :  22 	 length :  40
enqueue
avail :  23 	 front :  0 	 size :  23 	 length :  40
enqueue
avail :  24 	 front :  0 	 size :  24 	 length :  40
enqueue
avail :  25 	 front :  0 	 size :  25 	 length :  40
enqueue
avail :  26 	 front :  0 	 size :  26 	 length :  40
enqueue
avail :  27 	 front :  0 	 size :  27 	 length :  40
enqueue
avail :  28 	 front :  0 	 size :  28 	 length :  40
enqueue
avail :  29 	 front :  0 	 size :  29 	 length :  40
Dequeue
front : 1 	 size :  29 	 length :  40
Dequeue
front : 2 	 size :  28 	 length :  40
Dequeue
front : 3 	 size :  27 	 length :  40
Dequeue
front : 4 	 size :  26 	 length :  40
enqueue
avail :  30 	 front :  4 	 size :  26 	 length :  40
enqueue
avail :  31 	 front :  4 	 size :  27 	 length :  40
enqueue
avail :  32 	 front :  4 	 size :  28 	 length :  40
enqueue
avail :  33 	 front :  4 	 size :  29 	 length :  40
enqueue
avail :  34 	 front :  4 	 size :  30 	 length :  40
Dequeue
front : 5 	 size :  30 	 length :  40
Dequeue
front : 6 	 size :  29 	 length :  40
Dequeue
front : 7 	 size :  28 	 length :  40
Dequeue
front : 8 	 size :  27 	 length :  40
Dequeue
front : 9 	 size :  26 	 length :  40
Dequeue
front : 10 	 size :  25 	 length :  40
Dequeue
front : 11 	 size :  24 	 length :  40
Dequeue
front : 12 	 size :  23 	 length :  40
Dequeue
front : 13 	 size :  22 	 length :  40
Dequeue
front : 14 	 size :  21 	 length :  40
Dequeue
front : 15 	 size :  20 	 length :  40
Dequeue
front : 16 	 size :  19 	 length :  40
Dequeue
front : 17 	 size :  18 	 length :  40
Dequeue
front : 18 	 size :  17 	 length :  40
Dequeue
front : 19 	 size :  16 	 length :  40
Dequeue
front : 20 	 size :  15 	 length :  40
Dequeue
front : 21 	 size :  14 	 length :  40
Dequeue
front : 22 	 size :  13 	 length :  40
Dequeue
front : 23 	 size :  12 	 length :  40
Dequeue
front : 24 	 size :  11 	 length :  40
Dequeue
front : 25 	 size :  10 	 length :  40
Dequeue
front : 26 	 size :  9 	 length :  40
Dequeue
front : 27 	 size :  8 	 length :  40
Dequeue
front : 28 	 size :  7 	 length :  40
Dequeue
front : 29 	 size :  6 	 length :  40
Dequeue
front : 30 	 size :  5 	 length :  40
Dequeue
front : 31 	 size :  4 	 length :  40
Dequeue
front : 32 	 size :  3 	 length :  40
Dequeue
front : 33 	 size :  2 	 length :  40
Dequeue
front : 34 	 size :  1 	 length :  40
enqueue
avail :  35 	 front :  34 	 size :  1 	 length :  40
"""





    
