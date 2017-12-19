class ArrayStack:

	def __init__(self):
		self._stack =[]

	def __len__(self):
		return len(self._stack)

	def isEmpty(self):
		return __len__(self._stack) == 0

	def push(self, value):
		self._stack.append(value)

	def top(self):
		if self.isEmpty():
			raise Empty("Stack is empty")
		return self._stack[-1]

	def pop(self):
		if self.isEmpty():
			raise Empty("Stack is Empty")
		return self._stack.pop()





