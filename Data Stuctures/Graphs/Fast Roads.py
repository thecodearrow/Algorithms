
#https://www.codechef.com/ALPAST01/problems/FASTROAD
import sys
import math
from collections import defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

class Graph():
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v,cost):
        self.neighbours[u].append([v,cost])
        self.neighbours[v].append([u,cost])

    def djs(self,s,t):
        time=defaultdict(lambda:float("inf"))
        pq=[[0,s]]
        heapq.heapify(pq)
        while pq:
            minD,u=heapq.heappop(pq)
            for v,c in self.neighbours[u]:
                if(minD+c<time[v]):
                    time[v]=minD+c
                    heapq.heappush(pq,[time[v],v])


        if(time[t]==float("inf")):
            return -1
        return time[t]

t=int(input())
while t!=0:
    t-=1
    g=Graph()
    n,m,source,destination=[int(x) for x in input().split()]
    for i in range(m):
        u,v,l,speed=[int(x) for x in input().split()]
        g.addEdge(u,v,l/speed)
    print(g.djs(source,destination))
        

