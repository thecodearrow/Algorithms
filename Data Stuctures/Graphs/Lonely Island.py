#https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/lonelyisland-49054110/

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
    def __init__(self,source):
        self.neighbours=defaultdict(list)
        self.finished=[]
        self.indegree=defaultdict(lambda:0)
        self.outdegree=defaultdict(lambda:0)
        self.probabilty=defaultdict(lambda:0)
        self.probabilty[source]=1

    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.outdegree[u]+=1
        self.indegree[v]+=1

    def DFSVisit(self,u,visited):
        visited[u]=True
        for v in self.neighbours[u]:
            if(not visited[v]):
                self.DFSVisit(v,visited)
        self.finished.append(u)


       
    def printLonelyIsland(self):
        visited=defaultdict(lambda:False)
        finishedStack=self.finished[:]
        while finishedStack:
            u=finishedStack.pop()
            for v in self.neighbours[u]:
                self.probabilty[v]+=self.probabilty[u]*(1/self.outdegree[u])

            
        


n,m,source=[int(x) for x in input().split()]
g1=Graph(source)
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g1.addEdge(u,v)
   
g1.DFSVisit(source,defaultdict(lambda:False))
g1.printLonelyIsland()
probabilty=g1.probabilty
finishedStack=g1.finished
islands=set()
maxProbability=0
for u in finishedStack:
    if(g1.outdegree[u]==0):
        maxProbability=max(probabilty[u],maxProbability)
        islands.add(u)

epsilon=10**(-9)
final_answer=[]
for node in islands:
    diff=abs(maxProbability-probabilty[node])
    if(diff<=epsilon):
        final_answer.append(node)

final_answer=sorted(final_answer)
print(*final_answer)


