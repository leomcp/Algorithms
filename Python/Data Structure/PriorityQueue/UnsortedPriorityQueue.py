#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class UnsortedPriorityQueue(PriorityQueueBase):
	""" A min-oriented priority queue implemented wuth an unsorted list """
    #--------------------------------------------------------------------------------------
	def find_min(self):
		""" Return Position queue implemented with an unsorted list """
		if self.is_empty():
			raise Empty('Priority queue is empty')
		small = self._data.first()
		walk = self._data.after(small)
		while walk is not None:
			if walk.element() < small.element():
				small = walk 
			walk = self._data.after(walk)
		return small 
    #--------------------------------------------------------------------------------------
	def __init__(self):
		""" Create a new empty Priority Queue """
		self._data = PositionList()
    #--------------------------------------------------------------------------------------
	def __len__(Self):
		""" Return number of items in the priority queue """
		return len(self._data)
    #--------------------------------------------------------------------------------------
	def add(self, key, value):
		""" Add key-value pair """
		self._data.add_last(self._Item(key, value))
    #--------------------------------------------------------------------------------------
	def min(self):
		""" Return but do not remove (k, v) tuple with minimum key """
		p = self._find_min()
		item = self._data.delete(p)
		return (item._key, item._value)
    #--------------------------------------------------------------------------------------   
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
