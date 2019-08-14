
#https://www.spoj.com/problems/MST/
import sys
from collections import defaultdict
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass



class DisjointSet:
    def __init__(self,n):
        self.djset=[]
        for i in range(n+1):
            self.djset.append(i) #every node pointing to itself

    def find(self,node):
        while node!=self.djset[node]:
            node=self.djset[node]
        return node

    def union(self,u,v):
        #Lazy Union with no path compression! 
        if(u>v):
            u,v=v,u
        new_root=self.find(v)
        self.djset[self.find(u)]=new_root

   
    


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









		

		
				




		

