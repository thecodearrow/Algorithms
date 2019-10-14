#This Algorithm is not the most efficient for the problem

#This is roughly O(B^2*R)

#Optimal Algorithm is O(B*R)

from collections import defaultdict
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)
		
	def addEdge(self,u,v,bidirec=True):
		self.neighbours[u].append(v)
		if(bidirec):
			self.neighbours[v].append(u)
			
	def BFS(self,source,reqs):
		dist=defaultdict(lambda:float("inf"))
		dist[source]=0
		visited=defaultdict(lambda:False)
		visited[source]=True
		queue=[source]
		while queue:
			u=queue.pop(0)
			for v in self.neighbours[u]:
				if(not visited[v]):
					queue.append(v)
					visited[v]=True
					dist[v]=dist[u]+1
		cost=0
		max_cost=0
		for r in reqs:
			max_cost=max(dist[r],max_cost)
			
		return max_cost
		
		

def apartmentHunting(blocks, reqs):
	n=len(blocks)
	g=Graph()
	for i in range(n-1):
		g.addEdge(i,i+1)

	
	for i,block in enumerate(blocks):
		for r in reqs:
			if(block[r]):
				g.addEdge(i,r,bidirec=False)
				
	
	minCost=float("inf")
	ans=0
	l=float("inf")
	for i in range(n):
		current_cost=g.BFS(i,reqs)
		if(current_cost<minCost):
			minCost=current_cost
			ans=i

	return ans
		
	
		
