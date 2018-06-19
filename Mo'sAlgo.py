#Mo's Algorithm SPOJ DQUERY

import math
import functools
from collections import defaultdict
n=int(input())
block_size=int(math.sqrt(n-1))
answer={} #stores the answer for each query 

freq={} #contains freqs of elements in a 
freq=defaultdict(lambda:0,freq)

 

def cmp(a,b):
    x=a[0]//block_size
    y=b[0]//block_size
    #sorting by block_no
    if(x!=y):
        if(x<y):
            return -1
        else:
            return 1
    #sorting by R
    else:
        if(a[1]<b[1]):
            return -1
        else:
            return 1


a=[int(x) for x in input().split()]
q=int(input())
queries=[]
while(q!=0):
    q-=1
    temp=[int(x) for x in input().split()]
    queries.append(temp)
    

#sort based on block_no first and then sort based on R 
mo_queries=sorted(queries,key=functools.cmp_to_key(cmp))

#start end points
start=0
end=-1
count=0 #no. of distinct elements at that point

for q in mo_queries:
    L=q[0]-1
    R=q[1]-1
    while(start<L):
        ele=a[start]
        freq[ele]-=1
        start+=1  
        #updates count values from time to time! 
        if(freq[ele]==0):
            count-=1 
        
    while(start>L):
        start-=1
        ele=a[start]
        freq[ele]+=1
        if(freq[ele]==1):
            count+=1 
    
    while(end<R):
        end+=1
        ele=a[end]
        freq[ele]+=1 
        if(freq[ele]==1):
            count+=1 
    while(end>R): #because end got incremented
        ele=a[end]
        freq[ele]-=1 
        if(freq[ele]==0):
            count-=1 
        end-=1 
    answer[(L+1,R+1)]=count #stores count of distinct elements of each query
  

for q in queries:
    L=q[0]
    R=q[1]
    print(answer[(L,R)])


















