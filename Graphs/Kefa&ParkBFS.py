#BFS
#http://codeforces.com/contest/580/problem/C


cats={}
n,m=[int(x) for x in input().split()]
number_of_nodes=n
a=[int(x) for x in input().split()]
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

	def BFS(self,v):
		visited=defaultdict(lambda:False)
		visited[v]=True 
		visited_leaves=0 #contains visited leaf nodes 
		queue=[v]
		cat_count=defaultdict(lambda:0,{}) 
		parent={v:-1}
		while queue:
			#checking for a lead node 
			ele=queue.pop(0)
			
			if(cats[ele]):
				cat_count[ele]=cat_count[parent[ele]]+1 
			else:
				cat_count[ele]=0
			for v in self.neighbours[ele]:
				if(not visited[v]):
					if(cats[v]):
						if(cat_count[ele]+1<=m):
							queue.append(v)
							visited[v]=True
							parent[v]=ele
							
					else:
						queue.append(v)
						visited[v]=True
						parent[v]=ele
			if(len(self.neighbours[ele])==1 and ele!=1): #ele==1 is kefa's home!
				visited_leaves+=1
		return visited_leaves


	

g=Graph()
  

while(n!=1):
	n-=1
	u,v=[int(x) for x in input().split()]
	g.addEdge(u,v)


print(g.BFS(1))