#Connected Cell in a Grid

#https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict 
class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)


    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    

    def BFS_count(self,start,grid):
        count=0
        queue=[start]
        visited=defaultdict(lambda:False)
        visited[start]=True
        
        while queue:
            u=queue.pop(0)
            if(grid[u[0]][u[1]]==1):
                count+=1
                print(u,start)
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    visited[v]=True 


        return count 

    def BFSUtil(self,grid):
        count=[]
        visited=defaultdict(lambda:False)
        for u in self.neighbours:
            if(not visited[u]):
                if(grid[u[0]][u[1]]==1):
                    visited[u]=True 
                    count.append(self.BFS_count(u,grid))

        return max(count)


    
# Complete the maxRegion function below.
def maxRegion(grid):
    g=Graph()
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            current=grid[i][j]
            one=grid[i+1][j]
            two=grid[i][j+1]
            three=grid[i+1][j+1]
            if(one==1):
                g.addEdge((i,j),(i+1,j))
            if(two==1):
                g.addEdge((i,j),(i,j+1))
            if(three==1):
                g.addEdge((i,j),(i+1,j+1))
            
        
    return g.BFSUtil(grid)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

