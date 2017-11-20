class FirstClass:

	def __init__(self, name):

		self._name = name 

	def get_name(self):

		return self._name 


if __init__ == '__main__':

	fc = FirstClass('Mithilesh')
	print("Welcome ")
	print("Name :", fc.get_name())


