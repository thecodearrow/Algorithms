#https://www.codechef.com/problems/DISHOWN
import sys

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

class DisjointSet:
    def __init__(self,n,scores):
        self.scores=[0]+scores #1 indexing
        self.owner=[0]
        for i in range(1,n+1):
            self.owner.append(i) #every chef owns his dish initially

    def find(self,d):
        initial_dish=d
        while(d!=self.owner[d]):
            d=self.owner[d]
        owner=d
        
        #path compression
        while initial_dish!=self.owner[initial_dish]:
            initial_dish_copy=initial_dish
            initial_dish=self.owner[initial_dish]
            self.owner[initial_dish_copy]=owner

        return owner


    def union(self,u,v):
        owner_u=self.find(u)
        owner_v=self.find(v)
        if(self.scores[owner_u]>self.scores[owner_v]):
            self.owner[owner_v]=owner_u
        elif(self.scores[owner_v]>self.scores[owner_u]):
            self.owner[owner_u]=owner_v


t=int(input())
while t!=0:
    t-=1
    n=int(input())
    scores=[int(x) for x in input().split()]
    ds=DisjointSet(n,scores)
    q=int(input())
    for i in range(q):
        temp=[int(x) for x in input().split()]
        if(temp[0]==0):
            d1,d2=temp[1],temp[2]
            if(ds.find(d1)==ds.find(d2)):
                #same owner
                print("Invalid query!")
            else:
                ds.union(d1,d2)
        else:
            dish=temp[1]
            print(ds.find(dish))

    
