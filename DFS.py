from collections import defaultdict
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v,bidirec=False):
		#bidirectional True for undirected graph
		self.neighbours[u].append(v)
		if(bidirec):
			self.neighbours[v].append(u)

	def dfs_visit(self,v,visited):
		visited[v]=True 
		print(v)
		for ele in self.neighbours[v]:
			if(not visited[ele]):
				self.dfs_visit(ele,visited)

	def dfs(self,v):
		visited={}
		visited=defaultdict(lambda:False,visited)
		a=self.dfs_visit(v,visited)


g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)