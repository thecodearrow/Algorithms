
#https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/practice-problems/algorithm/monk-and-his-unique-trip/

#Partially Correct Only

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

sys.setrecursionlimit(100000)

class Graph():
    def __init__(self):
        self.neighbours=defaultdict(list)
        self.finished=[]
        self.scc=defaultdict(set)


    def addEdge(self,u,v):
        self.neighbours[u].append(v)

    def DFSVisit(self,u,visited):
        visited[u]=True
        for v in self.neighbours[u]:
            if(not visited[v]):
                self.DFSVisit(v,visited)
        self.finished.append(u)

    def DFSVisitK(self,u,visited,startNode):
        visited[u]=True
        for v in self.neighbours[u]:
            if(not visited[v]):
                self.scc[startNode].add(v)
                self.DFSVisitK(v,visited,startNode)
       

    def DFS(self,n):
        visited=defaultdict(lambda:False)
        for i in range(1,n+1):
            if(not visited[i]):
                self.DFSVisit(i,visited)

    def DFS_Custom(self,nodes):
        visited=defaultdict(lambda:False)
        for i in nodes:
            if(not visited[i]):
                self.DFSVisit(i,visited)

    def KosarajuAlgo(self,finishedStack):
        visited=defaultdict(lambda:False)
        number_of_components=0
        while finishedStack:
            u=finishedStack.pop()
            if(not visited[u]):
                self.DFSVisitK(u,visited,u)
                number_of_components+=1


        return self.scc,number_of_components

    def findLongestPathDistance(self,topoStack,nodes):
        distance=defaultdict(lambda:-float("inf"))
        maxD=0
        if(topoStack):
            source=topoStack[-1]
            distance[source]=0
            while topoStack:
                u=topoStack.pop()
                for v in self.neighbours[u]:
                    if(distance[v]<distance[u]+1):
                        distance[v]=distance[u]+1
                        maxD=max(distance[v],maxD)

        for n in nodes:
            maxD=max(maxD,distance[n])
        return maxD
        



n,m=[int(x) for x in input().split()]
g1=Graph()
g2=Graph()
edges=[]
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g1.addEdge(u,v)
    g2.addEdge(v,u)
    edges.append([u,v])

g1.DFS(n)
scc,nc=g2.KosarajuAlgo(g1.finished)
node_equivalent={}
for i in range(1,n+1):
    node_equivalent[i]=i

for k in scc:
    for node in scc[k]:
        node_equivalent[node]=k


#SCC Compression
g3=Graph()
nodes=set()
for u,v in edges:
    if(node_equivalent[u]!=node_equivalent[v]):
        g3.addEdge(node_equivalent[u],node_equivalent[v])
        nodes.add(node_equivalent[u])
        nodes.add(node_equivalent[v])

g3.DFS_Custom(nodes)


#Find the longest path of the graph and that's the state cost!
#https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/

print(g3.findLongestPathDistance(g3.finished,nodes))



