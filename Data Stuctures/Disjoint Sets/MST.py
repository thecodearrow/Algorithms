
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
        
def hasSingleCycle(array):
    # Write your code here.
    
    n=len(array)
    ds=DisjointSet(n)
    for i,jumps in enumerate(array):
        u=i
        v=(i+jumps)%n
        print(u,v)
        if(ds.find(u)==ds.find(v)):
            return True
        ds.union(u,v)
    
    
            
    return False
                
        
        
    
print(hasSingleCycle([2,3,1,-4,-4,2]))






		

		
				




		

