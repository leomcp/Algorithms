
class Vertex:
	def __init__(self, data):
		self.data = data 
		self.neighbours = []
		self.distance = 0 
		self.visited = 0 

	def add_neighbour(self, u):
		self.neighbours.append(u)
		self.neighbours.sort()


class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, v):
		if v not in self.vertices:
			self.vertices[v] = Vertex(v)

	def add_edge(self, u, v):
		if u not in self.vertices:
			self.add_vertex(u)
		if v not in self.vertices:
			self.add_vertex(v)
		self.vertices[u].add_neighbour(v)
		self.vertices[v].add_neighbour(u)

	def print_graph(self):
		if self.vertices:
			for key, value in self.vertices.items():
				print("{} : {}".format(key, value.neighbours))

	def _bfs(self, start_vertex):
		if start_vertex in self.vertices:

			q = []

			self.vertices[start_vertex].distance = 0 
			self.vertices[start_vertex].visited = True 

			q.append(start_vertex)

			while len(q)>0:
				top_vertex = q[0]
				top_vertex_distance = self.vertices[top_vertex].distance 
				self.vertices[top_vertex].visited = True 

				del(q[0])

				if self.vertices[top_vertex].neighbours:
					for neighbour in self.vertices[top_vertex].neighbours:
						if self.vertices[neighbour].visited == False:
							q.append(neighbour)
							self.vertices[neighbour].distance = top_vertex_distance + 1

	def get_shortest_distance(self, start_vertex, end_vertex):
		if start_vertex in self.vertices and end_vertex in self.vertices:
			self._bfs(start_vertex)
			return self.vertices[end_vertex].distance


if __name__ == "__main__":

	edges = ["AB", "AE", "ED", "EH", "DH", "HI", "IF", "FB", "FG", "GC", "GJ", "JF"]

	g = Graph()

	for edge in edges:
		g.add_edge(edge[0], edge[1])

	g.print_graph()

	# print("A : F --> {}".format(g.get_shortest_distance("A", "F")))

	# print("A : G --> {}".format(g.get_shortest_distance("A", "G")))

	print("B : C --> {}".format(g.get_shortest_distance("B", "C")))

	# print("A : C --> {}".format(g.get_shortest_distance("A", "C")))
