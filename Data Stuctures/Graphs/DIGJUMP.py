
#https://www.codechef.com/problems/DIGJUMP
 
import sys
import math
from collections import defaultdict
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

class Graph:
    def __init__(self):
        self.neighbours=defaultdict(set)

    def addEdge(self,u,v):
        if(v not in self.neighbours[u]):
            self.neighbours[u].add(v)
            self.neighbours[v].add(u)

    def BFS(self,n,s,at):
        visited=defaultdict(lambda:False)
        dist=defaultdict(lambda:float("inf"))
        visited[0]=True
        dist[0]=0
        queue=[0]
        added={}
        while queue:
            u=queue.pop(0)
            char=s[u]
            if(char not in added):
                added[char]=True
                for idx in at[char]:
                    g.addEdge(u,idx)
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)
                    dist[v]=dist[u]+1
        return dist[n-1]


 
 
s=input().strip()
at={}
n=len(s)
g=Graph()

at=defaultdict(list)
for i in range(n):
    at[s[i]].append(i)

for i in range(1,n):
    g.addEdge(i-1,i)

for i in range(n-1):
    g.addEdge(i,i+1)


print(g.BFS(n,s,at))

