#https://codeforces.com/contest/1234/problem/D
import sys
import math
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
 
s=input().strip()
n=len(s)
s=[0]+list(s)
BIT=[[0]*(n+1) for i in range(26)] #Maintain 26 BITs for every character a-z
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
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
 
def getTreeIndex(c):
    return ord(c)-97
 
q=int(input())
 
 
 
 
for i in range(1,n+1):
    index=getTreeIndex(s[i])
    update(index,i,1,n)
 
 
for q_i in range(q):
    temp=[x for x in input().split()]
    if(temp[0]=='1'):
        pos=int(temp[1])
        currentChar=s[pos]
        current_index=getTreeIndex(currentChar)
        update(current_index,pos,-1,n)
        newChar=temp[2]
        s[pos]=newChar
        new_index=getTreeIndex(newChar)
        update(new_index,pos,1,n)
        
    else:
        l=int(temp[1])
        r=int(temp[2])
        ans=0
        for index in range(0,26):
            count=rangeQuery(index,l,r) #count of c from [L,R]
            if(count>0):
                ans+=1
 
        print(ans)
 