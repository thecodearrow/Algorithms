#http://codeforces.com/contest/580/problem/C

#Tried DFS 
#Run Time Error Test Case 27 :(

cats={}
n,m=[int(x) for x in input().split()]
number_of_nodes=n
a=[int(x) for x in input().split()]
leaves=set() #set containing all non-leaf nodes
index=1 
for c in a:
	if(c==1):
		cats[index]=True 
	else:
		cats[index]=False
	index+=1


from collections import defaultdict
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v):
		self.neighbours[u].append(v) 
		self.neighbours[v].append(u)


	def dfs_visit(self,v,visited,catcount):
		goAhead=True
		visited[v]=True
		if(len(self.neighbours[v])==1):
			leaves.add(v) #adding leaf nodes to set
		if(cats[v]):
			catcount+=1
		else:
			catcount=0
		if(catcount>m):
			goAhead=False #stopping dfs along that path 
			visited[v]=False
		for i in self.neighbours[v]:
			if(not visited[i] and goAhead):
				self.dfs_visit(i,visited,catcount)
		return visited 

	def dfs(self,v):
		visited={}
		catcount=0 
		visited=defaultdict(lambda:False,visited)
		return self.dfs_visit(v,visited,catcount)


g=Graph()
  

while(n!=1):
	n-=1
	u,v=[int(x) for x in input().split()]
	g.addEdge(u,v)


visited_nodes=g.dfs(1)
ans=0 #possible restaurants
if(1 in leaves):
	leaves.remove(1) #removing kefa's house
for v in leaves:
	if(visited_nodes[v]):
		ans+=1

print(ans)

