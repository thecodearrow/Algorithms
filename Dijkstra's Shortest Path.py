from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)
	

	def addEdge(self,u,v,cost):
		self.neighbours[u].append((v,cost))
		self.neighbours[v].append((u,cost))

	def dijkstras(self,s):
		visited=defaultdict(lambda:False)
		distanceFromS=defaultdict(lambda:10**9+7) #setting all default values to infity 
		distanceFromS[s]=0
		remaining=[(0,s)]   #priority queue
		while remaining:
			minDist,minNode=heapq.heappop(remaining)  #extract min operation
			#now explore all neighbours of this node
			visited[minNode]=True
			for v,length in self.neighbours[minNode]:
				if(not visited[v]):
					greedyScore=minDist+length
					if(greedyScore<distanceFromS[v]):
						distanceFromS[v]=greedyScore #update distance
						heapq.heappush(remaining,(greedyScore,v))  #push updated node into priority queue



		return distanceFromS



g=Graph()
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,7,11)
g.addEdge(1,2,8)
g.addEdge(2,8,2)
g.addEdge(8,6,6)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(2,3,7)
g.addEdge(3,5,14)
g.addEdge(2,5,4)
g.addEdge(6,5,2)
g.addEdge(5,4,10)
g.addEdge(3,4,9)
print(g.dijkstras(0))










