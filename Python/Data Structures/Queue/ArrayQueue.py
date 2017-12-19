##--------------------------------------------------------------------------
##--------------------------------------------------------------------------
class ArrayQueue:
	"""
	queue implementation using a python list as underlying storage 
	"""
	DEFAULT_CAPACITY = 10 
    ##----------------------------------------------------------------------
	def __init__(self):
		
	   self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
       self._size = 0
       self._front = 0 
    ##----------------------------------------------------------------------
    def __len__(self):
    	## Return the number of elements in the queue 
    	return self._size 
    ##----------------------------------------------------------------------
    def is_empty(self):
        ## Return true if the queue is empty 
        return self._size == 0
    ##----------------------------------------------------------------------
    def first(self):
    	"""
    	Return (but do not remove) the element at the front of the queue 
    	Raise Empty exception if the queue is empty 
    	"""

    	if self.is_empty():
    		raise Empty('Queue is empty')
    	return self._data(self._front)
    ##----------------------------------------------------------------------
    def dequeue(self):
    	"""
    	Remove and return the first element of the queue (ie FIFO)

    	Raise Empty exception if the queue is empty 
    	"""

    	if self.is_empty():
    		raise Empty('Queue is empty')

    	answer = self._data[self._front]
    	self._data[self._front] = None
    	self.front = (self._front + 1) % len(self._data)
    	self._size -=1
    	return answer

    ##----------------------------------------------------------------------
    def enqueue(self, e):
    	## Add an element to the back of queue 
    	if self._size == len(self._data):
    		self._resize(2*len(self._data)) # double the array size 
    	avail = (self._front + self._size) % len(self._data)
    	self._data[avail] = e
    	self._size += 1

    ##----------------------------------------------------------------------
    def ._resize(self, cap):
    	## Resize to a new list of capacity >= len(self)

    	old = self._data 
    	self._data = [None] * cap
    	walk = self._front
    	for k in range(self._size):
    		self._data[k] = old[walk]
    		walk = (1+walk)%len(old)
    	self._front  = 0

    ##----------------------------------------------------------------------
    def displayQueue(self):
        if is_empty():
            raise Empty("Queue is empty")
        size = self.__len__()
        print("Queue :")
        for i in range(size):
            print("",self.data[i])
    ##----------------------------------------------------------------------
           
Queue = ArrayQueue()

Queue.enqueue(10)
Queue.enqueue(20)
Queue.enqueue(30)
Queue.enqueue(40)
Queue.enqueue(50)
Queue.enqueue(60)
Queue.enqueue(70)
Queue.enqueue(80)
Queue.enqueue(90)
Queue.enqueue(100)

Queue.displayQueue()

print("Length of Queue : ", Queue.len())
print("First element :", Queue.first())

print("Dequeue element :", Queue.dequeue())
Queue.displayQueue()


Queue.enqueue(110)
Queue.displayQueue()

Queue.enqueue(120)
Queue.enqueue(130)
Queue.enqueue(140)
Queue.enqueue(150)
Queue.enqueue(160)
Queue.enqueue(170)
Queue.enqueue(180)
Queue.enqueue(190)
Queue.enqueue(200)

Queue.displayQueue()
