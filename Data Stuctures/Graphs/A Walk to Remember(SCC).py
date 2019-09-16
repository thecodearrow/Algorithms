#https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/practice-problems/algorithm/a-walk-to-remember-qualifier2/description/

from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
        self.finished=[] #stack nodes by finish time
        self.scc=defaultdict(lambda:False)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        
    def DFSVisit(self,s,visited):
        visited[s]=True
        for v in self.neighbours[s]:
            if(not visited[v]):
                self.DFSVisit(v,visited)
        self.finished.append(s)
        
    
    def DFS(self,n):
        visited=defaultdict(lambda:False)
        for i in range(1,n+1):
            if(not visited[i]):
                self.DFSVisit(i,visited)
        
    def DFSVisitKosaraju(self,s,visited):
        visited[s]=True
        for v in self.neighbours[s]:
            if(not visited[v]):
                self.scc[s]=True
                self.scc[v]=True
                self.DFSVisitKosaraju(v,visited)
                
                
    def DFSKosaraju(self,n,finishedStack):
        visited=defaultdict(lambda:False)
        while finishedStack:
            u=finishedStack.pop()
            if(not visited[u]):
                self.DFSVisitKosaraju(u,visited)
                
n,m=[int(x) for x in input().split()]
g1=Graph()
g2=Graph() #reversed edges
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g1.addEdge(u,v)
    g2.addEdge(v,u)

g1.DFS(n)
g2.DFSKosaraju(n,g1.finished)
ans=[]
for i in range(1,n+1):
    if(g2.scc[i]):
        ans.append(1)
    else:
        ans.append(0)
        
print(*ans)
    