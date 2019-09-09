#https://www.spoj.com/problems/BUGLIFE/

#Bipartite Graph Problem
from collections import defaultdict
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def BFS(self,source,visited,color):
        queue=[source]
        visited[source]=True
        color[source]=0
        while queue:
            u=queue.pop(0)
            for v in self.neighbours[u]:
                if(visited[v]):
                    if(color[v]==color[u]):
                        return False
                elif(not visited[v]):
                    queue.append(v)
                    color[v]=1-color[u]
                    visited[v]=True
        return True

t=int(input())
modulo=10**9+7
for test_case_no in range(1,t+1):
    n,m=[int(x) for x in input().split()]
    g=Graph()
    for i in range(m):
        u,v=[int(x) for x in input().split()]
        g.addEdge(u,v)
    visited=defaultdict(lambda: False)
    color={}
    bipartite=False
    for i in range(1,n+1):
        if(not visited[i]):
            bipartite=g.BFS(i,visited,color)
            if(not bipartite):
                break

    print("Scenario #"+str(test_case_no)+":")
    if(not bipartite):
        print("Suspicious bugs found!")
    else:
        print("No suspicious bugs found!")

        