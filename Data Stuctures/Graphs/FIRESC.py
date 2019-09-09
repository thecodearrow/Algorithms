#https://www.codechef.com/problems/FIRESC/

from collections import defaultdict
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def BFS(self,source,visited):
        queue=[source]
        visited[source]=True
        nodes_visited=1
        while queue:
            u=queue.pop(0)
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    nodes_visited+=1
                    visited[v]=True
        return nodes_visited

t=int(input())
modulo=10**9+7
while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    g=Graph()
    for i in range(m):
        u,v=[int(x) for x in input().split()]
        g.addEdge(u,v)
    visited=defaultdict(lambda: False)
    fire_escapes=0 
    no_of_ways=1
    for i in range(1,n+1):
        if(not visited[i]):
            fire_escapes+=1
            no_of_ways*=g.BFS(i,visited)

    print(fire_escapes,no_of_ways%modulo)
        