# your code goes here
#https://www.spoj.com/problems/KOICOST/

#http://problem-solving-notes.blogspot.com/2011/07/spoj-koicost.html

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


n,m=[int(x) for x in input().split()]
edges=[]
costs=[]
ds=DisjointSet(n)
for i in range(m):
    u,v,c=[int(x) for x in input().split()]
    edges.append([u,v,c])
    costs.append(c)

sorted_edges=sorted(edges,key=lambda x:x[2],reverse=True) #By decreasing order of weights
#Approdaching the problem in reverse
costs=sorted(costs) #weights are unique 
cum_costs={} #sum of all weights < = w 
current_sum=0
for c in costs:
    current_sum+=c
    cum_costs[c]=current_sum
ans=0
for u,v,c in sorted_edges:
    leader_u=ds.find(u)
    leader_v=ds.find(v)
    if(leader_v!=leader_u):
        number_of_pairs=ds.size[leader_u]*ds.size[leader_v]
        d=cum_costs[c]
        ds.union(u,v)
        ans+=(number_of_pairs*d)



print(ans%10**9)







