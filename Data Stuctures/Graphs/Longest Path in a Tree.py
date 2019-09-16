#https://www.spoj.com/problems/PT07Z/

from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
        self.degree=defaultdict(lambda:0)
        self.maxDistance=0
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
        self.degree[u]+=1
        self.degree[v]+=1

    def DFS(self,source,visited,distance):
        visited[source]=True
        for node in self.neighbours[source]:
            if(not visited[node]):
                distance[node]=distance[source]+1
                self.maxDistance=max(self.maxDistance,distance[node])
                self.DFS(node,visited,distance)

    def BFS(self,source,visited):
        queue=deque([source])
        visited[source]=True
        maxDistance=0
        maxDistanceNode=source
        distance=defaultdict(lambda:0)
        distance[source]=0
        while queue:
            u=queue.popleft()
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    distance[v]=distance[u]+1
                    if(maxDistance<distance[v]):
                        maxDistance=max(maxDistance,distance[v])
                        maxDistanceNode=v
                    visited[v]=True
        return maxDistanceNode
    
n=int(input())
g=Graph()
for i in range(n-1):
    u,v=[int(x) for x in input().split()]
    g.addEdge(u,v)

if(n==1):
    print(1)
else:
    visited=defaultdict(lambda:False)
    farthest_node=g.BFS(1,visited) #finding a node from last level
    visited=defaultdict(lambda:False)
    g.DFS(farthest_node,visited,defaultdict(lambda:0))
    print(g.maxDistance)

    