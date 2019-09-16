#https://codeforces.com/problemset/problem/771/A

import sys
import math
from collections import defaultdict
from collections import deque
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


from collections import defaultdict
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
        self.edge_count=defaultdict(lambda:0)
    
    def addEdge(self,u,v):
        if(u!=v):
            #avoiding self loops
            self.neighbours[u].append(v)
            self.neighbours[v].append(u)
            self.edge_count[u]+=1
            self.edge_count[v]+=1

    def BFS(self,source,visited):
        #count the number of vertices and number of edges in the clique
        queue=deque([source])
        visited[source]=True
        vertices_count=0
        edges_count=0
        while queue:
            u=queue.popleft()
            vertices_count+=1
            edges_count+=self.edge_count[u]
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    visited[v]=True
        return vertices_count,edges_count



n,m=[int(x) for x in input().split()]
g=Graph()
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g.addEdge(u,v)

clique=True
visited=defaultdict(lambda:False)
for i in range(1,n+1):
    if(not visited[i]):
        vertices,edges=g.BFS(i,visited)
        #each vertex must be connected to all n-1 edges
        if(edges!=vertices*(vertices-1)):
            clique=False
            break
if(clique):
    print("YES")
else:
    print("NO")







    