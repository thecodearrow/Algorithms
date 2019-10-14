#https://www.codechef.com/ALPAST01/problems/SMCMP/

import sys
import math
from collections import defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

class DisjointSet:
    def __init__(self,n):
        self.parent=[0]
        self.rank=[0]
        for i in range(1,n+1):
            self.parent.append(i)
            self.rank.append(0)
    def find(self,node):
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])

        return self.parent[node]

    def union(self,u,v):
        l_u=self.find(u)
        l_v=self.find(v)
        if(l_v!=l_u):
            if(self.rank[l_u]>self.rank[l_v]):
                u,v=v,u 
                l_v,l_u=l_u,l_v

            if(self.rank[l_u]==self.rank[l_v]):
                self.rank[l_v]+=1

            self.parent[l_u]=l_v

n,q=[int(x) for x in input().split()]
ds=DisjointSet(n)
for i in range(q):
    idx,u,v=[int(x) for x in input().split()]
    if(idx==1):
        ds.union(u,v)
    else:
        l_u=ds.find(u)
        l_v=ds.find(v)
        if(l_v!=l_u):
            print("No")
        else:
            print("Yes")



