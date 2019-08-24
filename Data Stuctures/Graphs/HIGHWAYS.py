#https://www.spoj.com/problems/HIGHWAYS/

import sys
from collections import defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v,cost):
        self.neighbours[u].append([v,cost])
        self.neighbours[v].append([u,cost])

    def dijkstra(self,s,t):
        visited=defaultdict(lambda: False)
        distanceFromS=defaultdict(lambda: 10**9+7) #init to INFINITY
        distanceFromS[s]=0
        heap=[(0,s)] #V-X
        heapq.heapify(heap)
        while heap:
            minDist,x=heapq.heappop(heap)
            if(x==t):
                break
            if(not visited[x]):
                visited[x]=True
                for v,cost in self.neighbours[x]:
                    if(not visited[v]):
                        if(distanceFromS[x]+cost<distanceFromS[v]):
                            distanceFromS[v]=distanceFromS[x]+cost
                            heapq.heappush(heap,(distanceFromS[v],v))

        if(distanceFromS[t]!=10**9+7):

            return distanceFromS[t]
        else:
            return "NONE"



test_cases=int(input())
for test in range(test_cases):
    n,m,s,t=[int(x) for x in input().split()]
    g=Graph()
    for i in range(m):
        u,v,c=[int(x) for x in input().split()]
        g.addEdge(u,v,c)
    print(g.dijkstra(s,t))
