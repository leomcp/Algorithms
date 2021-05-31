from __future__ import print_function
from collections import deque

class Vertex:

	def __init__(self, data):
		self.data = data	
		self.distance = -1
		self.visited = False 
		self.parent = None
		self.neighbours = []

	def addNeighbour(self, v):
		if v not in self.neighbours:
			self.neighbours.append(v)

class UDGraph:

	def __init__(self, n, m, edges, s):
		self.n = n
		self.m = m
		self.edges = edges
		self.s = s
		self.vertices = {}
		self.jsf = "" # Journey So Far ....

		self.build()
		self.printGraph()
		self.bfs()

	def build(self):
		for n in range(1, self.n+1):
			self.vertices[n] = Vertex(n)
		for edge in edges:
			self._addEdge(edge[0], edge[1])

	def _addEdge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].addNeighbour(v)
			self.vertices[v].addNeighbour(u)

	def printGraph(self):
		print("-"*30)
		print("UDGraph : ")
		if self.vertices:
			for v in sorted(self.vertices):
				print("{} --> {}".format(v, self.vertices[v].neighbours))

	def bfs(self):
		print("-"*30)
		if s in self.vertices:
			self._bfs()
			if self.jsf:
				print("BFS : {}".format(self.jsf))

	def _bfs(self):
		q = deque()
		q.append(self.s)
		self.vertices[self.s].distance = 0
		self.vertices[self.s].visited = True

		while len(q) > 0:
			head_v = q.popleft()
			self.jsf = self.jsf + " " +  str(head_v)

			for neighbour in self.vertices[head_v].neighbours:
				if self.vertices[neighbour].visited == False:
					self.vertices[neighbour].distance = self.vertices[head_v].distance + 1
					self.vertices[neighbour].visited = True
					self.vertices[neighbour].parent = head_v
					q.append(neighbour)

	def shortestPath(self, e):
		print("-"*30)
		print("Shortest Path BFS From {} to {} : ".format(self.s, e))
		if self.s in self.vertices and e in self.vertices:
			if self.vertices[e].distance == -1:
				print("Path does not exists... ")
			else:
				print("Distance = {}".format(self.vertices[e].distance))
				print("Path --> ", end=" ")
				path = []
				path.append(e)
				parent = self.vertices[e].parent
				while parent!= self.s:
					path.append(parent)
					parent = self.vertices[parent].parent
				path.append(self.s)
				for _ in range(len(path)):
					print(path.pop(), end=" ")
				print()

if __name__ == "__main__":

	# Total number of vertices (from 1 to n)
	n = 12
	# Total number of edges 
	m = 11
	edges = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 5], [5, 6], [5, 7], [7, 8], [4, 8], [7, 9], [9, 10]]
	s = 1  # start Vertex
	e = 10 # End Vertex

	udg = UDGraph(n, m, edges, s)

	udg.shortestPath(10)
	udg.shortestPath(8)
	udg.shortestPath(6)
	udg.shortestPath(11)

	print("-"*30)

"""

OUTPUT : 

------------------------------
UDGraph : 
1 --> [2, 3]
2 --> [1, 3, 4]
3 --> [1, 2, 5]
4 --> [2, 8]
5 --> [3, 6, 7]
6 --> [5]
7 --> [5, 8, 9]
8 --> [7, 4]
9 --> [7, 10]
10 --> [9]
11 --> []
12 --> []
------------------------------
BFS :  1 2 3 4 5 8 6 7 9 10
------------------------------
Shortest Path BFS From 1 to 10 : 
Distance = 5
Path -->  1 3 5 7 9 10 
------------------------------
Shortest Path BFS From 1 to 8 : 
Distance = 3
Path -->  1 2 4 8 
------------------------------
Shortest Path BFS From 1 to 6 : 
Distance = 3
Path -->  1 3 5 6 
------------------------------
Shortest Path BFS From 1 to 11 : 
Path does not exists... 
------------------------------
"""

