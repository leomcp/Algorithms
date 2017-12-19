#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class Progression:
	""" Iterator producing a generic progression

	Default iterator produces the whole numbers 0, 1, 2 .....
	"""

	def __init__(self, start = 0):
		""" Initialize current to the first value of the progression """
		self._current = start 

	def _advance(self):
		""" Update self._current to a new value 

		This should be overidden by a subclass to customize progrssion

		By convention, if current is set to None, this designates the end of a finite progrssion 
		"""
		self._current += 1 

	def __next__(self):
		""" Return the next element, or else raise StopIteration error """
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current 
			self._advance()
			return answer 

	def __iter__(self):
		""" By cinvention, an iterator  must return itself as an iterator """
		return self

	def print_progression(self, n):
		""" Print next n values of the regression """
		print(''.join(str(next(self)) for i in range(n)))
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class ArithmeticProgression(Progression):
	""" Iterator producing an arithmetic progrssion """

	def __init__(self, increment = 1, start = 0):
		""" Create a new arithmetic progrssion 

		increment --> the fixed constant to add to each term (default 1)
		start --> the first term  of the progression (default 0)
		"""
		super().__init__(start)
		self._increment = increment 

	def _advance(self):
		""" Update current value by adding the fixed increment """
		self._current += self._increment 
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class GeometricProgrssion(Progression):
	""" Iterator producing a geometric progression """

	def __init__(self, base = 2, start = 1):
		""" Create a new geometric progrssion 

		base --> fixed constant multiplied to each item 
		start --> first term of the progression
		"""
		super().__init__(start)
		self._base = base 

	def _advance(self):
		""" Update current value by muliplying it by the base value """
		self._current *= self._base
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class FibinacciProgression(Progression):
	""" Iterator producing a generalized Fibonacci progression """

	def __init__(self, first = 0, second = 1):
		""" Create a new fibonacci progression 

		first --> first term of the progrssion
		second --> second term of the progrssion
		"""
		super().__init__(first)
		self._prev = second-first


	def _advance(self):
		""" Update current value by taking sum of previous two """
		self._prev, self._current = self._current, self._prev + self._current
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	print('Default Progression')
	Progression().print_progression(10)

	print('Arithmetic Progression with increment 5: ')
	ArithmeticProgression(5).print_progression(10)

	print('Arithmetic Progression with increment 5 and start 2: ')
	ArithmeticProgression(5, 2).print_progression(10)

	print('Geometric Progression with default base: ')
	GeometricProgrssion(3).print_progression(10)

	print('Geometric Progression with base 3: ')
	GeometricProgrssion(3).print_progression(10)

	print('Fibinacci progression with default start values: ')
	FibinacciProgression().print_progression(10)

	print('Fibonacci progression with start values 4 and 6: ')
	FibinacciProgression(4, 6).print_progression(10)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

"""
OUTPUT :

Default Progression
0123456789
Arithmetic Progression with increment 5: 
051015202530354045
Arithmetic Progression with increment 5 and start 2: 
271217222732374247
Geometric Progression with default base: 
13927812437292187656119683
Geometric Progression with base 3: 
13927812437292187656119683
Fibinacci progression with default start values: 
0112358132134
Fibonacci progression with start values 4 and 6: 
461016264268110178288

"""
