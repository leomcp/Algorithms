class Vertex:

	def __init__(self, data):
		self.data = data 
		self.neighbours = []
		self.visited = False 
		self.distance = 0 

	def addNeighbour(self, v):
		if v not in self.neighbours:
			self.neighbours.append(v)

class UDGraph:

	def __init__(self):
		self.vertices = {}

	def _addVertex(self, v):
		self.vertices[v] = Vertex(v)

	def _addEdge(self, v1, v2):
		if v1 not in self.vertices:
			self._addVertex(v1)
		if v2 not in self.vertices:
			self._addVertex(v2)

		self.vertices[v1].addNeighbour(v2)
		self.vertices[v2].addNeighbour(v1)

	def buildGraph(self, edges):
		for edge in edges:
			self._addEdge(edge[0], edge[1])

	def printGraph(self):
		if self.vertices:
			for v in sorted(self.vertices):
				print("{} --> {}".format(v, self.vertices[v].neighbours))

	def _bfs(self, start_v):
		q = []
		q.append(start_v)

		while len(q)>0:
			head_v = q[0]
			self.vertices[head_v].visited = True 

			del(q[0])

			for n in self.vertices[head_v].neighbours:
				if self.vertices[n].visited == False:
					q.append(n)
					self.vertices[n].visited = True 
					self.vertices[n].distance = self.vertices[head_v].distance + 1

	def findShortestDistance(self, start_v, end_v):
		if self.vertices:
			if start_v not in self.vertices:
				return 
			if end_v not in self.vertices:
				return 

			self._bfs(start_v)
			print("Shortest Distance between {} and {} : {}".format(start_v, end_v, self.vertices[end_v].distance))


if __name__ == "__main__":


	edges = ["AB", "BD", "AC", "CD", "DE", "DF"]

	g = UDGraph()

	g.buildGraph(edges)
	g.printGraph()

	g.findShortestDistance("A", "F")


"""
OUTPUT : 


A --> ['B', 'C']
B --> ['A', 'D']
C --> ['A', 'D']
D --> ['B', 'C', 'E', 'F']
E --> ['D']
F --> ['D']
Shortest Distance between A and F : 3

"""

