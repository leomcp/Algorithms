
class Vertex:

	def __init__(self, data):
		self.data = data 
		self.neighbours = []
		self.visited = False 

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

	def dfs(self, start_v):
		if self.vertices:
			if start_v not in self.vertices:
				print("{} not found in Graph")
				return None
			else:
				print("DFS : ")
				self._dfs(start_v)
				print()

	def _dfs(self, start_v):

		q = []
		q.append(start_v)
		self.vertices[start_v].visited = True

		while len(q)>0:
			top_v = q.pop()
			
			print(top_v, end=" ") 

			for n in self.vertices[top_v].neighbours:
				if self.vertices[n].visited == False:
					q.append(n)
					self.vertices[n].visited = True 

if __name__ == "__main__":

	g = UDGraph()

	edges = ["AB", "BD", "AC", "CD", "DE", "DF"]

	g.buildGraph(edges)
	g.printGraph()

	g.dfs("A")


"""
OUTPUT : 

A --> ['B', 'C']
B --> ['A', 'D']
C --> ['A', 'D']
D --> ['B', 'C', 'E', 'F']
E --> ['D']
F --> ['D']
DFS : 
A C D F E B 

"""
