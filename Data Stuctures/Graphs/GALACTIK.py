#https://www.codechef.com/problems/GALACTIK
 
 
from collections import defaultdict

visited=defaultdict(lambda:False)
n,m=[int(x) for x in input().split()]
cost=defaultdict()
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)
 
	def addEdge(self,u,v):
		#bidirectional
		self.neighbours[u].append(v)
		self.neighbours[v].append(u)

	def BFS(self,s,n,visited):
		queue=[s]
		visited[s]=True 
		mini=10**7

		while queue:
			u=queue.pop(0)
			mini=min(cost[u],mini)
			for v in self.neighbours[u]:
				if(v not in visited):
					visited[v]=True
					queue.append(v)
					mini=min(cost[v],mini)

		return mini

 
	
g=Graph()
for i in range(m):
	u,v=[int(x) for x in input().split()]
	g.addEdge(u,v)
 
 
for i in range(1,n+1):
	value=int(input())
	if(value>=0):
		cost[i]=value 
	else:
		cost[i]=10**7 #infinity



minimums=[]

for i in range(1,n+1):
	if(i not in visited):
		m=g.BFS(i,n,visited)
		minimums.append(m)

l=len(minimums)
possible=True

for i in minimums:
	if(i>=10**6):
		possible=False
		break


if(l==1):
	print(0)
elif(not possible):
	print(-1)
else:
	global_min=min(minimums)
	ans=global_min*(l-1)+sum(minimums)-global_min
	print(ans)
 