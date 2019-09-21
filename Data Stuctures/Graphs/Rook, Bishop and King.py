

#https://codeforces.com/problemset/problem/370/A
import sys
import math
from collections import defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

class Graph():
    def __init__(self,type):
        self.neighbours=defaultdict(list)
        if(type==0):
            #King
            self.addKing()
            
        elif(type==1):
            #Rook
            self.addRook()

        else:
            #Add Bishop moves
            self.addBishop()

    def addKing(self):
        for x in range(1,9):
            for y in range(1,9):
                for i in range(-1,2):
                    for j in range(-1,2):
                        pos_x=x+i
                        pos_y=y+j
                        if(self.isValid(pos_x,pos_y)):
                            self.addEdge([x,y],[pos_x,pos_y])
    def addRook(self):
        for x in range(1,9):
            for y in range(1,9):
                for pos_y in range(1,9):
                    if(pos_y!=y):
                        self.addEdge([x,y],[x,pos_y])
        for x in range(1,9):
            for y in range(1,9):
                for pos_x in range(1,9):
                    if(pos_x!=x):
                        self.addEdge([x,y],[pos_x,y])

    def addBishop(self):
        #Absolute diff(x2-x1)==Absolute diff (y2-y1)
        for x in range(1,9):
            for y in range(1,9):
                for posx in range(1,9):
                    for posy in range(1,9):
                        if(abs(x-posx)==abs(y-posy)):
                            self.addEdge([x,y],[posx,posy])

    def addEdge(self,u,v):
        pos1=self.ltos(u)
        pos2=self.ltos(v)
        self.neighbours[pos1].append(pos2)
        self.neighbours[pos2].append(pos1)

    def ltos(self,l):
        return str(l[0])+":"+str(l[1])
    def isValid(self,x,y):
        if(x<1 or x>8):
            return False
        if(y<1 or y>8):
            return False
        return True

    def stol(self,s):
        return [int(s[0]),int(s[2])]

    def BFS(self,source,destination):
        source=self.ltos(source)
        destination=self.ltos(destination)
        visited=defaultdict(lambda:False)
        distance=defaultdict(lambda:float("inf"))
        distance[source]=0
        visited[source]=True
        queue=[source]
        parent=defaultdict(lambda:None)
        while queue:
            u=queue.pop(0)
            if(u==destination):
                break
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    parent[v]=u
                    distance[v]=distance[u]+1
                    queue.append(v)
        if(distance[destination]==float("inf")):
            return 0
        return(distance[destination])
        


x1,y1,x2,y2=[int(x) for x in input().split()]
source=[x1,y1]
destination=[x2,y2]
king=Graph(0)
rook=Graph(1)
bishop=Graph(2)
print(rook.BFS(source,destination),bishop.BFS(source,destination),king.BFS(source,destination))
