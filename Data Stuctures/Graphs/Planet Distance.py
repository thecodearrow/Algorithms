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

#8th Aug 2019 Detected point at which cycle occurs

#Got to still print the cycle

#Then, use BFS to calculate dist from cycle 

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
		queue=[s]
		parent={}
		traversed=defaultdict(lambda:False)
		parent[s]=None
		cycle=set()
		while queue:
			u=queue.pop()
			if(not visited[u]):
				print(u)
				visited[u]=True
			for v in self.neighbours[u]:
				if(not visited[v]):
					queue.append(v)
					parent[v]=u
				elif(visited[v] and parent[u]!=v):
					current=v 
					while current not in cycle:
						cycle.add(v)
						current=parent[current]

			
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

	print(c)
	

		


