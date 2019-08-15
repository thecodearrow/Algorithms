#https://www.spoj.com/problems/CSTREET/

import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


class DisjointSet():
    def __init__(self,n):
        self.parent=[]
        self.rank=[]
        for i in range(n+1):
            self.parent.append(i)
            self.rank.append(0) #default rank

    def find(self,node):
        if(node==self.parent[node]):
            return node
        node=self.find(self.parent[node]) #path compression
        return node

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(self.rank[leader_u]>self.rank[leader_v]):
            u,v=v,u
            leader_u,leader_v=leader_v,leader_u
        if(leader_u!=leader_v):
            self.parent[leader_u]=leader_v #update pointer
            self.rank[leader_v]+=1 #update rank


t=int(input())
while t!=0:
    t-=1
    price_per_unit=int(input())
    n=int(input())
    ds=DisjointSet(n)
    m=int(input())
    edges=[]
    for i in range(1,m+1):
        u,v,l=[int(x) for x in input().split()]
        cost=l*price_per_unit
        edges.append([u,v,cost])

    edges=sorted(edges,key=lambda x:x[2]) #sort by cost
    ans_min_cost=0
    count=0
    for u,v,c in edges:
        if(count==n-1):
            break
        if(ds.find(u)!=ds.find(v)):
            count+=1
            ans_min_cost+=c
            ds.union(u,v)

    print(ans_min_cost)






