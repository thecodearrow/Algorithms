#https://code.google.com/codejam/contest/4384486/dashboard#s=p0

"""
Input 
 	
Output 
 
2
5
1 2
2 3
3 4
2 4
5 3
3
1 2
3 2
1 3

Case #1: 1 0 0 0 1
Case #2: 0 0 0

"""
from collections import defaultdict

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v):
		self.neighbours[u].append(v)
		self.neighbours[v].append(u)

	def BFS(self,s):
		visited=defaultdict(lambda:False)
		visited[s]=True
		queue=[s]
		level={s:0}
		while queue:
			u=queue.pop(0)
			for v in self.neighbours[u]:
				if(not visited[v]):
					visited[v]=True 
					queue.append(v)
					level[v]=level[u]+1

		return level

	def DFS_cycle(self,s):
		visited=defaultdict(lambda:False)
		visited[s]=True
		queue=[s]
		parent={}
		parent[s]=None
		while queue:
			u=queue.pop()
			for v in self.neighbours[u]:
				if(visited[v] and parent[v]!=u):
					#cycle found
					current_node=v 
					cycle=[]
					while(parent[current_node]!=v):
						cycle.append(current_node)
						current_node=parent[current_node]
				elif(not visited[v]):
					visited[v]=True
					queue.append(v)
					parent[v]=u
		return cycle


t=int(input())
for test_case in range(1,t+1):
	q=int(input())
	g=Graph()
	for query in range(q):
		u,v=[int(x) for x in input().split()]
		g.addEdge(u,v)

	c=g.DFS_cycle(1)
	new=Graph()
	isCycle={}
	for i in c:
		isCycle[i]=True

	

		


