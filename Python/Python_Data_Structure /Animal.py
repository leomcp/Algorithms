class Animal :

	__name = None 
	__height = 0
	__weight = 0 
	__sound = 0

	def set_name(self, name ):
		self.__name = name

	def get_name(self):
		return self.__name

	# Constructor 

	def __init__(self, name, height, weight, sound):

		self.__name = name 
		self.__height = height 
		self.__weight = weight 
		self.__sound = sound 

	def get_type(self):
		print("Animal")

	def toString(self):
		return "Mithilesh"
		#return "{} is {} cm tall {} kilograms and sound {}".format(self.__name, self.__height, self.__weight, self.__sound)

 cat = Animal('Mithilesh', 33, 10, 'Meow')

 print(cat.toString())		