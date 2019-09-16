#https://codeforces.com/problemset/problem/755/C

import sys
import math
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

class DisjointSet():
    def __init__(self,n):
        self.parent=[0]
        for i in range(1,n+1):
            self.parent.append(i)
        
    def find(self,node):
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(leader_u!=leader_v):
            self.parent[leader_u]=leader_v
n=int(input())
relatives=[int(x) for x in input().split()]
ds=DisjointSet(n)
edge_index=[i for i in range(n+1)]
for i,r in enumerate(relatives):
    #print(edge_index[i+1],r)
    ds.union(edge_index[i+1],r)

trees=0
seen=set()
for i in range(1,n+1):
    leader=ds.find(i)
    if(leader not in seen):
        seen.add(leader)
        trees+=1

print(trees)







    
