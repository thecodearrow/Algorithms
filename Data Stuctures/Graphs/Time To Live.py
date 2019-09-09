#https://www.spoj.com/problems/GCPC11J/
#https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts

from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(set)
        self.degree=defaultdict(lambda:0)
    
    def addEdge(self,u,v):
        self.neighbours[u].add(v)
        self.neighbours[v].add(u)
        self.degree[u]+=1
        self.degree[v]+=1

    def BFS(self,source,visited):
        queue=deque([source])
        visited[source]=True
        maxDistance=0
        distance=defaultdict(lambda:0)
        distance[source]=0
        while queue:
            u=queue.popleft()
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    distance[v]=distance[u]+1
                    maxDistance=max(maxDistance,distance[v])
                    visited[v]=True
        return maxDistance

    def findRootByEatingLeaves(self,n):
        if(n==1):
            return 0
        leaves=[]
        for i in range(n):
            if(self.degree[i]==1):
                leaves.append(i)
        while n>2:
            #while only 1 or 2 nodes remain
            n-=len(leaves)
            nextLeaves=[]
            for l in leaves:
                node=self.neighbours[l].pop() 
                self.neighbours[node].remove(l) #remove current leaf node
                self.degree[node]-=1
                if(self.degree[node]==1):
                    nextLeaves.append(node)
            leaves=nextLeaves
        root=leaves[0] #can be 1 or 2 nodes
        return root
        
t=int(raw_input())
for test_case_no in range(1,t+1):
    n=int(raw_input())
    g=Graph()
    g1=Graph()
    for i in range(n-1):
        u,v=[int(x) for x in raw_input().split()]
        g.addEdge(u,v) #for first BFS 
        g1.addEdge(u,v) #for second BFS
    #find root
    root=g.findRootByEatingLeaves(n)
    visited=defaultdict(lambda:False)
    optimal_hops=g1.BFS(root,visited)
    #optimal longest distance from root node
    print(optimal_hops)
        
