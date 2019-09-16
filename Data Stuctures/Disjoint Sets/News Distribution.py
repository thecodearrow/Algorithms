#https://codeforces.com/problemset/problem/1167/C

#TLE -.-

import sys
import math
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

class DisjointSet():
    def __init__(self,n):
        self.parent=[0]
        self.size=[1]
        self.rank=[0]
        for i in range(1,n+1):
            self.parent.append(i)
            self.rank.append(0)
            self.size.append(1)
        
    def find(self,node):
        #path compression
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        #union by rank
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(leader_u!=leader_v):
            if(self.rank[leader_u]>self.rank[leader_v]):
                u,v=v,u 
                leader_v,leader_u=leader_u,leader_v
            self.parent[leader_u]=leader_v
            self.size[leader_v]+=self.size[leader_u]
            if(self.rank[leader_u]==self.rank[leader_v]):
                self.rank[leader_v]+=1


n,m=[int(x) for x in input().split()]
ds=DisjointSet(n)
for i in range(m):
    temp=[int(x) for x in input().split()]
    k=temp[0]
    if(k!=0):
        first_edge=temp[1]
    for idx in range(2,k+1):
        node=temp[idx]
        ds.union(first_edge,node)
        first_edge=node

answer=0
for i in range(1,n+1):
    print(ds.size[ds.find(i)],end=' ')









    
