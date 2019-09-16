#https://www.spoj.com/problems/PT07Y/
from collections import defaultdict
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def DFS(self,source,visited,parent):
        visited[source]=True
        for node in self.neighbours[source]:
            if(visited[node] and parent[source]!=node):
                return True
            if(not visited[node]):
                parent[node]=source
                self.DFS(node,visited,parent)
        return False

    
    
n,m=[int(x) for x in input().split()]
#A tree has N-1 edges and is a connected, acyclic graph
g=Graph()
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g.addEdge(u,v)

if(m!=n-1):
    print("NO")
else:
    visited=defaultdict(lambda:False)
    parent=defaultdict(lambda:None)
    isCycle=(g.DFS(1,visited,parent))
    connected=True
    for i in range(1,n+1):
        if(not visited[i]):
            connected=False
    if(not connected or isCycle):
        print("NO")
    else:
        print("YES")



    