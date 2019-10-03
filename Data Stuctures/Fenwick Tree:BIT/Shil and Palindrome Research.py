#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/shil-and-palindrome-research/


import sys
import math
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 

def takeInput():
    return [int(x) for x in input().strip().split()]
 
n,q=takeInput()
s=input().strip()
s=[0]+list(s)
BIT=[[0]*(n+1) for i in range(26)] #Maintain 26 BITs for every character a-z

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
 

 
for i in range(1,n+1):
    index=getTreeIndex(s[i])
    update(index,i,1,n)


for q_i in range(q):
    temp=[x for x in input().split()]
    if(temp[0]=='1'):
        pos=int(temp[1])
        old_char=s[pos]
        update(getTreeIndex(old_char),pos,-1,n)
        char=temp[2]
        s[pos]=char
        update(getTreeIndex(char),pos,1,n)

    else:
        l,r=int(temp[1]),int(temp[2])
        #Get the count of all chars in [L,R]
        #The count has to be even for it to be a palindrome
        #Only odd count is permitted for odd length segment
        segment_length=r-l+1
        evenLength=(segment_length%2)==0
        palindrome=True
        odd_count=0
        for idx in range(26):
            count=rangeQuery(idx,l,r)
            if(evenLength):
                if(count%2==1):
                    #Count cannot be odd! 
                    palindrome=False
                    break
            else:
                if(count%2==1 and odd_count>0):
                    palindrome=False
                    break
                elif(count%2==1):
                    #One allowed
                    odd_count+=1

        if(palindrome):
            print("yes")
        else:
            print("no")



 