#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
class ArrayStack:
	""" LIFO Stack implementaion using a python list as an underlying storage """

	def __init__(self):
		""" Create an empty stack """
		self._data = []

	def __len__(self):
		""" Return the number of elemenr in the stack """
		return len(self._data)

	def is_empty(self):
		""" Return's True if the stack is empty """
		return len(self._data) == 0

	def push(self, e):
		""" Add element e to the top of stack """
		self._data.append(e)  # new item stored at the end of the list 

	def pop(self):
		""" Remove and return the element from the top of stack 

		Raise an exception if the stack is empty
		"""

		if self.is_empty():
			raise Empty('Stack is empty')

		return self._data.pop() # removes the last element from the list 

	def print_stack(self):
		""" Prints all the element of the stack
        
        Raise empty exception if stack is empty
		"""

		if self.is_empty():
			raise Empty('Stack is empty')

		print('Stack --> ')

		for i in range(len(self._data)):
			print('',self._data[i])


def reverse_file(filename):
		""" Overwrite given file with its content line-by-line reversed """

		S = ArrayStack()
		original = open(filename)
		for line in original:
			S.push(line.rstrip('\n'))  # re-insert newlines when writing
		original.close()

		# now we overwrite with contents in LIFO order 
		output = open(filename, 'w')  # reopening file overwrites original 
		while not S.is_empty():
			output.write(S.pop()+'\n') #re-insert newline charactes 
		output.close()

if __name__ == '__main__':

	reverse_file('kafka.txt')


