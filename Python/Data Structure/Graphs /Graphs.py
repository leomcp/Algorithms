# --------------------------nested vertex class --------------------------------
class Vertex:
	# Leightweight vertex structure for a graph 
	__slots__ = '_element'

	def __init__(self,x):
		self._element = x

	def element(self):
		# retruns elements associated with this vertex 
		return self._element

	def __hash__(self): # will allow vertes to be map/set key 
		return hash(id(self))

#-----------------nested class Edge ---------------------------------------------
class Edge:

	__slots__ = '_origin', '_destination', '_element '

	def __init__(self, u, v, x):

		self._origin=u
		self._destination = v
		self._element = x

	def endpoints(self):
		return (self._origin, self._destination)

	def opposite(self, v):
		self._destination if v os self._origin else self._origin

	def element(self):
		return self._element

	def __hash__(self):
		return hash((self._origin, self._destination))

		