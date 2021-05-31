from __future__ import print_function
import sys 

from collections import deque

class Vertex:

	def __init__(self, data):
		self.data = data
		self.neighbours = []
		self.visited = False

	def addNeighbour(self, u):
		if u not in self.neighbours:
			self.neighbours.append(u)

class UDGraph:

	def __init__(self, n, edges):
		self.vertices = {}
		self.n = n
		self.edges = edges
		self.jsf = ""
		self.cc = 0

		self.build()
		self.printGraph()

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

	def connectedComponents(self):
		print("-"*30)
		print("Connected Components (CC) : ")
		if self.vertices:
			for v in sorted(self.vertices):
				if self.vertices[v].visited == False:
					self.cc = self.cc + 1
					self.dfs(v)
		print("No of Connected Components : {}".format(self.cc))

	def dfs(self, v):
		print("DFS on {}-CC: ".format(self.cc), end="")
		if v in self.vertices:
			self._dfs(v)
			print(self.jsf)
			self.jsf = ""

	def _dfs(self, v):
		q = deque()
		q.append(v)
		self.vertices[v].visited = True

		while len(q) > 0:
			head_v = q.pop()
			self.jsf = self.jsf + " " + str(head_v)

			for neighbour in self.vertices[head_v].neighbours:
				if self.vertices[neighbour].visited == False:
					self.vertices[neighbour].visited = True
					q.append(neighbour)

if __name__ == "__main__":

	# Total number of Nodes from 1 to n
	n = 15
	# Edges
	edges =[[1, 2], [1, 3], [2, 4], [2, 3], [3, 5], [5, 6], [5, 7],
			[7, 8], [7, 9],[4, 8], [9, 10], [11, 12], [11, 13], 
			[12, 13], [13, 14], [13, 15]] 

	udg = UDGraph(n, edges)
	udg.connectedComponents()

	print("-"*30)

"""

OUTPUT : 

------------------------------
UDGraph :
1 --> [2, 3]
2 --> [1, 4, 3]
3 --> [1, 2, 5]
4 --> [2, 8]
5 --> [3, 6, 7]
6 --> [5]
7 --> [5, 8, 9]
8 --> [7, 4]
9 --> [7, 10]
10 --> [9]
11 --> [12, 13]
12 --> [11, 13]
13 --> [11, 12, 14, 15]
14 --> [13]
15 --> [13]
------------------------------
Connected Components (CC) : 
DFS on 1-CC:  1 3 5 7 9 10 8 4 6 2
DFS on 2-CC:  11 13 15 14 12
No of Connected Components : 2
------------------------------

"""