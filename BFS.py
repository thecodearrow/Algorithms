from collections import defaultdict

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v,bidirec=True):
		#bidirectional True for undirected graph
		self.neighbours[u].append(v)
		if(bidirec):
			self.neighbours[v].append(u)

	def BFS(self,s):
		queue=[s]
		visited=defaultdict(lambda:False)
		level={s:0}  #breadth-wise search! 
		parent={s:-1} #useful to trace back the shortest path
		visited[s]=True 
		while queue:
			u=queue.pop(0)
			#u=queue.pop() #And the code is now DFS as it becomes a stack ;)
			print(u,end=" ")
			for v in self.neighbours[u]:
				if(not visited[v]):
					queue.append(v)
					visited[v]=True
					level[v]=level[u]+1 
					parent[v]=u
			




g=Graph()
g.addEdge(3,2)
g.addEdge(2,3)
g.addEdge(1,2)
g.BFS(1)
print()
g.BFS(2)
print()
g.BFS(3)