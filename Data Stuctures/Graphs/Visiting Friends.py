
#https://www.codechef.com/problems/MCO16405

#Partial Correct Answer

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

sys.setrecursionlimit(10**5)
class Graph:
    def __init__(self,n,population):
        self.neighbours=defaultdict(list)
        self.finished=[]
        self.distance=defaultdict(lambda:0) #dp
        self.population=[0]+population #1 indexing
        for i in range(1,n+1):
            self.distance[i]=self.population[i]

        self.scc=defaultdict(set)

    def addEdge(self,u,v):
        self.neighbours[u].append(v)

    def DFSVisit(self,u,visited):
        visited[u]=True
        for v in self.neighbours[u]:
            if(not visited[v]):
                self.DFSVisit(v,visited)

        self.finished.append((u))

    def DFS(self,n):
        visited=defaultdict(lambda:False)
        for i in range(1,n+1):
            if(not visited[i]):
                self.DFSVisit(i,visited)

    def DFSKosaraju(self,u,visited,startNode):
        visited[u]=True
        for v in self.neighbours[u]:
            if(not visited[v]):
                self.DFSKosaraju(v,visited,startNode)
                self.scc[startNode].add(v)

    
    def findSCC(self,finishedStack):
        #Works only for Reversed Graph
        #Kosaraju's Algorithm
        visited=defaultdict(lambda:False)
        while finishedStack:
            u=finishedStack.pop()
            if(not visited[u]):
                self.DFSKosaraju(u,visited,u)





    def maxReach(self):
        #DP Solution that starts processing nodes in reverse
        reverse_graph=self.finished[::-1]
        while reverse_graph:
            u=reverse_graph.pop()
            self.distance[u]=self.population[u]
            maxD=0
            for v in self.neighbours[u]:
                maxD=max(maxD,self.distance[v])
            self.distance[u]+=maxD






n,m=[int(x) for x in input().split()]
population=[int(x) for x in input().split()]
g=Graph(n,population)
g_reverse=Graph(n,population)
edges=[]
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g.addEdge(u,v)
    g_reverse.addEdge(v,u)
    edges.append([u,v])
g.DFS(n)
g_reverse.findSCC(g.finished)

scc=g_reverse.scc

g_final=Graph(n,population)
node_equivalent={}
for i in range(1,n+1):
    node_equivalent[i]=i #initially

#Update population

for i in range(1,n+1):
    if(len(scc[i])!=0):
        nodes=list(scc[i])
        for vertex in nodes:
            g_final.population[i]+=g_final.population[vertex]

for u,v in edges:
    ##Find SCC and compress all nodes that belong to a SCC into one node
    if(v in scc[node_equivalent[u]]):
        node_equivalent[v]=node_equivalent[u]
    elif(u in scc[node_equivalent[v]]):
        node_equivalent[u]=node_equivalent[v]
    
    if(node_equivalent[u]!=node_equivalent[v]):
        #not in same scc
        g_final.addEdge(node_equivalent[u],node_equivalent[v])
  
g_final.DFS(n)
g_final.maxReach()
for i in range(1,n+1):
    node=node_equivalent[i]
    print(g_final.distance[node],end=" ")


