#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
"""
Operator Overloading and Python's Special methods :

Python's built-in class provide natural semantics for many operators. For Eg, the syntax a+b invokes 
addition for numeric types, yet concatenation for sequence types.

Operator Overloading : This is done by implementing a specially named method. In particular, the + 
operator is overloaded by implementing a method named __add__, which takes the right-hand operand as 
parameter and which returns the result of the expression.
That us, the syntax , a+b, is converted to a method call on object a of the form, a.__add__(b).

Non-Operator Overloads :
Python relies on specially named methods to control the behaviour of various other fuctionality, 
when applied to user-defined classes. For example, the syntax, str(foo), is formaly a call to the 
constructor for the string class. If the parameter is an instance of a user-defined class, the 
original authors of the string class could not have known how that instance should be portrayed..
So, the string constructor calls a specially named method, foo.__str__(), that must return an 
appropriate string representation.

Similar special methods are used to determine how to construct an int, float, or cool based on a 
parameter from a user-defined class.

Implied Methods :
There are some operators that have a default definations provided by Python, in the absense of 
special methods, and there are some operators whose definations are drived from others. 
For example, the __bool__ method, ehich supports the syntax if foo:;, has default semantics so that 
every object other than None is evaluated as True.

EXAMPLE : MULTIDIMENSIONAL VECTOR CLASS :

To demonstrate the use of operator overloading vis special methods, we provide an implementation of a
Vector class, representing the coordinates of a vector in a multidimensional space. 
List does not provide an appropirate abstraction for geometric vector.Inernally, our vector relies u
pon an instance of a list, named _coords, as its storage mechanism.

"""
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
class Vector:

	""" Represent a vector in a multidimensional space """

	def __init__(self, d):
		""" Create d-dimensional vector of zeros """
		self._coords = [0] * d

	def __len__(self):
		""" Return the dimension of the vector """
		return len(self._coords)

	def __getitem__(self, j):
		""" Return jth coordinate of vector to given value """
		return self._coords[j] 

	def __setitem__(self, j, val):
		""" Set the jth coordinate of vector to given value """
		self._coords[j] = val

	def __add__(self, other):
		""" Return sum of two vectors """

		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result 

	def __eq__(self, other):
		""" Return True if vector has some coordinates as other """
		return self._coords == other._coords

	def __ne__(self, other):
		""" Return True if vector differs from other """
		return not self == other  # rely on existing __eq__ defination

	def __str__(self):
		""" Produce string representation of vector """
		return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

if __name__ == '__main__':

	v = Vector(4)

	print("Lenght : ", v.__len__())
	print("Get Item : ", v.__getitem__(2))
	v.__setitem__(3, 6)
	print("Get Item : ", v.__getitem__(3))
	v.__add__((0, 0, 0, 20))
	print("Vector : ", v.__str__())

"""
# OUTPUT :
Lenght :  4
Get Item :  0
Get Item :  6
Vector :  <0, 0, 0, 6>
"""


