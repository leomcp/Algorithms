#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
"""
STACKS :

A stack is a collection of objects that are inssrted and removed accoirding to the Last-in, first-out (LIFO) 
principle. A user may insert objects into a stack at any time, but may only acess or remove the most recently
inserted object that remains (at the  so-called 'top' of the stack). 

STACK ABSTRACT DATA TYPE :
Stack is an abstract data type (ADT) such that an instance S supports the following two methods :

  S.push(e) : Add element e to the top of stack S 
  S.pop() : Remove and return the top element from the Stack S; an error occurs if the stack is empty
  Additionaly,
  S.top() : Return a reference to the top element of stack S, without removing it, an error occurs if the stack
            is empty
  S.is_empty() : Return True if Stack S does not contain any elements 
  len(s) : Return number of element in Stack S.

"""
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
class ArrayStack:
	""" LIFO Stack implementaion using a Python list as underlying storage """

	def __init__(self):
		""" Create an empty stack """
		self._data = []  # non public list instance 

	def __len__(self):
		""" Return the number if elements in the stack """
		return len(self._data)

	def is_empty(self):
		""" Return True if the stack is empty """
		return len(self._data) == 0

	def push(self, e):
		""" Add element e to the top of stack """
		self._data.append(e)   # new item stored at end of list 

	def top(self):
		""" Return (but do not remove) the element at the top of the stack 

		Raise Empty exception if the stack is empty 
		"""

		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]  # the last item in the list 

	def pop(self):
		""" Remove and return the element from the top pf the stack 

		Raise Empty exception if the stack is empty.
		"""

		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()  # remove last item from list 

	def print_Stack(self):
		""" Prints all the element from the stack 

        Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty')
		print('Stack --> ')
		for i in range(len(self._data)):
			print('',self._data[i])
		print()

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	stack = ArrayStack()

	for i in range(10):
		stack.push(i)

	stack.print_Stack()

	print('Top : ', stack.pop())

	stack.print_Stack()
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
"""
OUTPUT :
Stack --> 
 0
 1
 2
 3
 4
 5
 6
 7
 8
 9

Top :  9
Stack --> 
 0
 1
 2
 3
 4
 5
 6
 7
 8
"""




