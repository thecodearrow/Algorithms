
#https://www.spoj.com/problems/MST/
import sys
from collections import defaultdict
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

   
    


n,m=[int(x) for x in input().split()]
sorted_nodes=[]
for i in range(m):
    u,v,c=[int(x) for x in input().split()]
    sorted_nodes.append([u,v,c])

sorted_nodes=sorted(sorted_nodes,key=lambda x:x[2]) #sorting based on costs
ds=DisjointSet(n)
count=0  #need n-1 edges in MST
min_cost=0
for u,v,c in sorted_nodes:
    if(count==n-1):
        break
    if(ds.find(u)!=ds.find(v)):
        #no cycle
        min_cost+=c
        count+=1
        ds.union(u,v)
        #print(u,v,ds.djset)
print(min_cost)
#print(ds.djset)









		

		
				




		

