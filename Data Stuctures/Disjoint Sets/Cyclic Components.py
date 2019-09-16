#https://codeforces.com/problemset/problem/977/E

#Can be made easier using DFS/BFS too 
#But here I have used DSU to solve it 

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
        for i in range(1,n+1):
            self.parent.append(i)
        
    def find(self,node):
        #doing path compression in a non recursive fashion!
        node_copy=node
        while(node!=self.parent[node]):
            node=self.parent[node]
        parent_node=node
        while node_copy!=self.parent[node_copy]:
            next_node=self.parent[node_copy]
            self.parent[node_copy]=parent_node
            node_copy=next_node
        return parent_node

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(leader_u!=leader_v):
            self.parent[leader_u]=leader_v


n,m=[int(x) for x in input().split()]
ds=DisjointSet(n)
cycled_components=set()
degree=defaultdict(lambda:0)
for i in range(m):
    u,v=[int(x) for x in input().split()]
    degree[u]+=1
    degree[v]+=1
    uL=ds.find(u)
    vL=ds.find(v)
    if(uL==vL):
        #belong to same component
        if(uL not in cycled_components):
            cycled_components.add(uL)
    elif(uL not in cycled_components and vL not in cycled_components):
        ds.union(u,v)

#Also check for degree of vertices. According to the given definition, degree should be 2 for a node in cycle
for i in range(1,n+1):
    iL=ds.find(i)
    if(iL in cycled_components):
        if(degree[i]!=2):
            cycled_components.remove(iL)

print(len(cycled_components))            










    