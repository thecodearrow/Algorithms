#https://www.hackerrank.com/contests/university-codesprint-5/challenges/ab-special-points

#TLE :(

from collections import defaultdict

class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def BFS(self,s,middle_bound,a,b):
        visited=defaultdict(lambda:False)
        visited[s]=True 
        queue=[s]
        lb=10**9
        ub=-10**9
        while queue:
            u=queue.pop(0)
            current=len(self.neighbours[u])
            lb=min(lb,current)*a
            ub=max(ub,current)*b
            if(lb<middle_bound and middle_bound<ub):
                return [lb,ub]
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)

        return [lb,ub]



g=Graph()
n,m,a,b=[int(x) for x in input().split()]
for i in range(m):
    u,v=[int(x) for x in input().split()]
    g.addEdge(u,v)



special_count=0
for i in range(1,n+1):
    nbrs=g.neighbours[i]
    middle_bound=len(nbrs)
    [lower_bound,upper_bound]=g.BFS(i,middle_bound,a,b)    
    if(lower_bound<middle_bound and middle_bound<upper_bound):
        special_count+=1

print(special_count)

