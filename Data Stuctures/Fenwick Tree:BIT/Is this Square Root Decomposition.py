

#https://www.codechef.com/ALPAST01/problems/VERYHARD

import sys
import math
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 

def takeInput():
    return [int(x) for x in input().strip().split()]
 
n,q,k=takeInput()
a=takeInput()
a=[0]+list(a)
BIT=[[0]*(n+1) for i in range(5)] #Remainders can only be from 0 to 4 (Given K ranges from 1 to 5 only)

def update(treeIndex,pos,val,n):
    tree=BIT[treeIndex]
    while pos<=n:
        tree[pos]+=val
        pos+=(pos&(-pos))
 
def query(treeIndex,pos):
    ans=0
    tree=BIT[treeIndex]
    while pos>0:
        ans+=tree[pos]
        pos-=(pos&(-pos))
    return ans
def rangeQuery(treeIndex,left,right):
    return query(treeIndex,right)-query(treeIndex,left-1)
 

 
for i in range(1,n+1):
    remainder=a[i]%k
    update(remainder,i,1,n)



for q_i in range(q):
    temp=takeInput()
    if(temp[0]==1):
        pos=temp[1]
        x=temp[2]
        oldRemainder=a[pos]%k
        update(oldRemainder,pos,-1,n) #Remove old remainder
        a[pos]+=x
        newRemainder=a[pos]%k
        update(newRemainder,pos,1,n) #Update new remainder

    else:
        l,r,rem=temp[1],temp[2],temp[3]
        print(rangeQuery(rem,l,r))

    
    


 