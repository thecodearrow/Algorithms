#https://codeforces.com/contest/1234/problem/C
import sys
import math
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v):
        #Let's keep it directed for simplicity and there's no point in going back the pipes!
        self.neighbours[u].append(v) 

    def BFS(self,destination):
        queue=[1]
        visited=defaultdict(lambda:False)
        while queue:
            u=queue.pop(0)
            if(u==destination):
                return True
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)

        return False

t=int(input())

while t!=0:
    t-=1
    n=int(input())
    row1=input()
    row2=input()
    row1=[int(x) for x in list(row1)]
    row2=[int(x) for x in list(row2)]
    #Simplifying 2 to 1 and the rest to 3 since they're equivalent
    for i,r in enumerate(row1):
        if(r==1 or r==2):
            row1[i]=1
        else:
            row1[i]=3
    for i,r in enumerate(row2):
        if(r==1 or r==2):
            row2[i]=1
        else:
            row2[i]=3
    

    maze=[0]+row1+row2+[0] #2*n+1 is the destination node
    g=Graph()
    for i in range(1,2*n+1):
        if(maze[i]==1):
            #Make a path forward
            if(i!=n):
                #Edge case end of row1
                g.addEdge(i,i+1)
        #If there are 3s above and below
        #Make a path diagonally either from row1 to row2 or row2 to row1
        if(i<=n):
            if(maze[i]==3 and maze[i+n]==3):
                g.addEdge(i,i+n+1)
        else:
            if(maze[i]==3 and maze[i-n]==3):
                if(i!=2*n):
                    #Edge case end of row2
                    g.addEdge(i,i-n+1)


    destination=2*n+1
    if(g.BFS(destination)):
        print("YES")
    else:
        print("NO")












