"""
https://codeforces.com/contest/151/problem/D

You can build a graph with positions in sting as a nodes and equality in any substring 
of length k as edges. Lets denote e the number of components in the graph. The answer is m^e.
"""
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
        self.rank=[0]
        for i in range(1,n+1):
            self.parent.append(i)
            self.rank.append(0)

    def find(self,node):
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(leader_v!=leader_u):
            if(self.rank[leader_u]>self.rank[leader_v]):
                u,v=v,u
                leader_u,leader_v=leader_v,leader_u
            if(self.rank[leader_u]==self.rank[leader_v]):
                self.rank[leader_v]+=1
            self.parent[leader_u]=leader_v #pointing u to v 


        



n,m,k=[int(x) for x in input().split()]
ds=DisjointSet(n)
for start in range(1,n-k+2):
    end=start+k-1
    for i in range(math.ceil(k/2)):
        ds.union(start,end)
        start+=1
        end-=1

no_of_components=0
seen=set()
for i in range(1,n+1):
    leader=ds.find(i)
    if(leader not in seen):
        seen.add(leader)
        no_of_components+=1

modulo=10**9+7
print(pow(m,no_of_components,modulo))

    
