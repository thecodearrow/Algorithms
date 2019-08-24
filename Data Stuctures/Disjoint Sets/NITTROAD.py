# your code goes here
 
#https://www.spoj.com/problems/NITTROAD/
#TLE :/
 
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
            self.size.append(1)
            self.rank.append(0)

    def find(self,node):
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(self.rank[leader_u]>self.rank[leader_v]):
            u,v=v,u
            leader_u,leader_v=leader_v,leader_u
        if(self.rank[leader_u]==self.rank[leader_v]):
            self.rank[leader_v]+=1
        self.parent[leader_u]=leader_v #pointing u to v 
        self.size[leader_v]+=self.size[leader_u]


        
 
 
t=int(input())
for test_case in range(t):
    n=input()
    while len(n)==0:
        n=input() 
    n=int(n)
    ds=DisjointSet(n)
    snapshot={}
    for i in range(1,n):
        h1,h2=[int(x) for x in input().split()]
        snapshot[i]=[h1,h2] #capturing road i
 
    q=int(input())
    total_pairs=(n*(n-1))/2
    ans=[]
    roads_added=0
    queries=[]
    removed_edges=set()
    for i in range(q):
         r=input()
         queries.append(r)
         if(r!="Q"):
            removed_edges.add(int(r.split()[1]))

    for i in range(1,n):
        h1,h2=snapshot[i]
        if(i not in removed_edges):
            h1_leader=ds.find(h1)
            h2_leader=ds.find(h2)
            if(h1_leader!=h2_leader):
                total_pairs-=(ds.size[h1_leader]*ds.size[h2_leader])
                ds.union(h1,h2)
        
    for r in queries[::-1]:
         #solving it backwards
        if(r=="Q"):
           ans.append(total_pairs)
        else:
            r=int(r.split()[1])
            h1,h2=snapshot[r]
            h1_leader=ds.find(h1)
            h2_leader=ds.find(h2)
            if(h1_leader!=h2_leader):
                total_pairs-=(ds.size[h1_leader]*ds.size[h2_leader])
                ds.union(h1,h2)

            

               

    for a in ans[::-1]:
        print(int(a))     
           
 
    print() #blank line
