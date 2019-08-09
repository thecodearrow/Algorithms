#Graphs as a Service

#https://www.facebook.com/hackercup/problem/862237970786911/

import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass

from collections import defaultdict
import heapq

class Graph:
    def __init__(self,V):
        self.n=V
        self.adjacencyMatrix=[]
        self.shortestPathMatrix=[]
        self.INF=10**9+7
        for i in range(V):
            self.adjacencyMatrix.append([])
            self.shortestPathMatrix.append([])
            for j in range(V):
                if(i==j):
                    self.adjacencyMatrix[i].append(0)
                    self.shortestPathMatrix[i].append(0)
                else:
                    self.adjacencyMatrix[i].append(self.INF)
                    self.shortestPathMatrix[i].append(self.INF)


    def addEdge(self,u,v,cost):
        self.adjacencyMatrix[u-1][v-1]=cost 
        self.adjacencyMatrix[v-1][u-1]=cost 
        self.shortestPathMatrix[u-1][v-1]=cost 
        self.shortestPathMatrix[v-1][u-1]=cost 

    def floydWarshall(self):
        V=self.n 
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    self.shortestPathMatrix[i][j]=min(self.shortestPathMatrix[i][j],self.shortestPathMatrix[i][k]+self.shortestPathMatrix[k][j])

        return self.shortestPathMatrix



        

    

t=int(input())
for test_case in range(1,t+1):
    n,m=[int(x) for x in input().split()]
    g=Graph(n)
    inputs=[]
    for i in range(m):
        a,b,w=[int(x) for x in input().split()]
        g.addEdge(a,b,w)
        inputs.append([a,b,w])
    shortest_path=g.floydWarshall()
    possible=True

    for p in range(m):
        a,b,w=inputs[p][0],inputs[p][1],inputs[p][2]
        if(shortest_path[a-1][b-1]<w):
            possible=False
            break

    if(possible):
        print("Case #"+str(test_case)+": "+str(m))
        for p in range(m):
            print(inputs[p][0],inputs[p][1],inputs[p][2])
    else:
        print("Case #"+str(test_case)+": Impossible")






		

		
				




		

