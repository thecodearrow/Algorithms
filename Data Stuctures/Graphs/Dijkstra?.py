#http://codeforces.com/problemset/problem/20/C

import heapq
INF=1<<60
class Graph:
	def __init__(self,n):
		self.neighbours=[[] for x in range(n+1)]
	

	def addEdge(self,u,v,cost):
		self.neighbours[u].append((v,cost))
		self.neighbours[v].append((u,cost))

	def dijkstra(self,s,d,n):
		parent={s:None}
		distanceFromS=[INF for x in range(n+1)] #FML! WA TEST CASE 31 because my infinity's value was too low. 
		distanceFromS[s]=0
		visited=[False for x in range(n+1)]
		remaining=[(0,s)]
		while remaining:
			minDist,minNode=heapq.heappop(remaining)
			if(not visited[minNode]):
				visited[minNode]=True
				if(visited[d]):
					return parent
				for v,length in self.neighbours[minNode]:
					if(not visited[v]):
						greedyScore=minDist+length
						if(greedyScore<distanceFromS[v]):
							distanceFromS[v]=greedyScore
							parent[v]=minNode
							heapq.heappush(remaining,(greedyScore,v))

		return parent




n,m=[int(x) for x in input().split()]
g=Graph(n)
for i in range(m):
	u,v,cost=[int(x) for x in input().split()]
	g.addEdge(u,v,cost)

path=g.dijkstra(1,n,n)

if(n not in path):
	print(-1)
else:
	ans=[]
	current=n
	while current!=None:
		ans.append(current)
		current=path[current]

	print(*ans[::-1])
