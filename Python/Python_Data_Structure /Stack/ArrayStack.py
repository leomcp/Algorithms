class ArrayStack:

	def __init__(self):
		self._data = []

	def  len(self):
		return len(self._data)

	def isEmpty(self):
		return len(self._data) == 0

	def push(self, e):
		self._data.append(e)

	def top(self):

		if self.isEmpty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):

		if self.isEmpty():
			raise Empty('Stack is empty')
		return self._data.pop()



s = ArrayStack()
##------------------------------------------------------------
##------------------------------------------------------------
if s.isEmpty == True:
	print ("Stack is empty")
else:
	print("Stack is not empty")
##------------------------------------------------------------
## Adding some data 
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
##------------------------------------------------------------
##------------------------------------------------------------
## Length of the stack 
print("Stack length :",s.len())
##------------------------------------------------------------
print("Stack top element : ", s.top())
##------------------------------------------------------------
##------------------------------------------------------------


	

