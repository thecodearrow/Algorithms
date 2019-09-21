
#https://codeforces.com/problemset/problem/266/B
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
    def __init__(self):
        self.neighbours=defaultdict(list)
        for x in range(1,9):
            for y in range(1,9):
                for i in range(-1,2):
                    for j in range(-1,2):
                        pos_x=x+i
                        pos_y=y+j
                        if(self.isValid(pos_x,pos_y)):
                            self.addEdge([x,y],[pos_x,pos_y])

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
    def whatMove(self,move1,move2):
        x1,y1=self.stol(move1)
        x2,y2=self.stol(move2)
        if(x1==x2):
            if(y1<y2):
                return "U"
            else:
                return "D"
        elif(y1==y2):
            if(x1<x2):
                return "R"
            else:
                return "L"
        elif(x2==x1-1 and y2==y1-1):
            return "LD"
        elif(x2==x1-1 and y2==y1+1):
            return "LU"
        elif(x2==x1+1 and y2==y1-1):
            return "RD"
        elif(x2==x1+1 and y2==y1+1):
            return "RU"


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
        print(distance[destination])
        ans=[]
        start=destination
        while parent[start]!=None:
            ans.append(self.whatMove(parent[start],start))
            start=parent[start]
        for a in ans[::-1]:
            print(a)



s=input().strip()
d=input().strip()
ref={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
source=[ref[s[0]],int(s[1])]
destination=[ref[d[0]],int(d[1])]
g=Graph()
g.BFS(source,destination)
