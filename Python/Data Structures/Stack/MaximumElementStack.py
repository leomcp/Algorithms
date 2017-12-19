class ArrayStack:

	def __init__(self):
		self._data = []

	def len(self):
		return len(self._data)

	def isEmpty(self):
		return self._data == 0 

	def top(self):
		if self.isEmpty():
			raise Empty("Stack is empty")
		else:
			return self._data[-1]

    def push(self, e):
    	self._data.append(e)

    def pop(self):
    	if self.isEmpty():
    		raise Empty("Stack is Empty")
    	return self.data.pop()
    

method = {
	
}

mainStack = ArrayStack()
trackStack = ArrayStack()

n = input()

for i range(n):

	option = input()
	if option !=2:
		methodnum = input()



	 







