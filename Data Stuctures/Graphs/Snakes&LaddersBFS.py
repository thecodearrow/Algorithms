#https://www.geeksforgeeks.org/snake-ladder-problem-2/
"""
Given a snake and ladder board, find the minimum number of dice throws
 required to reach the destination or last cell from source or 1st cell

 """
from collections import defaultdict

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v,bidirec=False):

		self.neighbours[u].append(v)
		if(bidirec):
			self.neighbours[v].append(u)

	def BFS(self,s,d):
		queue=[s]
		visited={}
		visited=defaultdict(lambda:False)
		level={s:0}
		parent={s:-1}
		visited[s]=True 
		while queue:
			u=queue.pop(0)
			#print(u,end=" ")
			for v in self.neighbours[u]:
				if(not visited[v]):
					queue.append(v)
					visited[v]=True
					level[v]=level[u]+1
					parent[v]=u
		

		print("The game can be won in",level[30]," moves.")

		while(d!=-1):
			print(d,end="<-")
			d=parent[d]


ladders={3:22,5:8,11:26,20:29}
snakes={27:1,21:9,17:4,11:7}

g=Graph()

#adding board edges

for u in range(1,25):
	for i in range(1,7):
		v=u+i
		if(v in snakes):
			v=snakes[v]
		if(v in ladders):
			v=ladders[v]
		g.addEdge(u,v)



g.BFS(1,30)
