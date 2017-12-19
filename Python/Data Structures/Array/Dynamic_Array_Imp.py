import ctypes # provides low level array 

class DynamicArray:

	# A dynamic array class akins to a simplified Python List 
    
    def __init__(self):
    	self._n =0 # counts actual elements 
    	self._capacity = 1 # default array capacity 
    	self._A = self._make_array(self._capacity) # loe -level array 

    def __len__(self):
    	# return's number of elements stored in array 
    	return self._n

    def __getitem__(self, k):
    	#returns elements at index k 

    	if not 0<=k<self._n:
    		raise IndexError("Invalid index")
    	return self._A[k] # retrieve from array 

    def append(self, obj):
    	# Add object to the end of array 

    	if self._n == self._capacity:
    		self._resize(2* self._capacity)
    	self._A[self._n] = obj
    	self._n +=1

    def _resize(self, c):
    	# Resize the array to capacuty c 
    	B = selef._make_array(c)  # new bigger array 
    	for k in range(self._n):
    		B[k] = self._A[k]
    	self._A=B
    	self._capacity=c

    def _make_array(self, c):
    	# Return new array with capacity c 
    	return ((c * ctypes.py_object))  # ctypes documentaion 

    def print_array(self):
    	len = self.__len__()
    	print("Array elements :")
    	for k in range(len):
    		print self._A[k]


array = DynamicArray()

print "",array.__len__()

array.append(10)
array.append(20)
array.append(30)
array.append(40)
array.append(50)
array.append(60)
array.append(70)
array.append(80)
array.append(90)
array.append(100)

print "",array.__len__()


array.print_array()

print "Index of 30 element :", array.__getitem__(10)







	
	
	



