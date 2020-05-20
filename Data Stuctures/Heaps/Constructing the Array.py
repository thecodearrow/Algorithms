#https://codeforces.com/contest/1353/my


import sys
import math
from collections import Counter,defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
    
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
 
 
 
 
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[0]*n
    status=True
    i=1
    lengths=[(-(n-1),0)] #   (length of max zeros, start_index)  sorted by max length and min start index
    heapq.heapify(lengths)
    for i in range(1,n+1):
        #print(lengths)
        l,si=heapq.heappop(lengths)
        l*=-1
        ei=si+l
        mid=(si+ei)//2
        #left segment
        l1=(mid-1)-si
        if(l1>=0):
            heapq.heappush(lengths,(-l1,si))
 
        #right segments
        l2=ei-(mid+1)
        if(l2>=0):
            heapq.heappush(lengths,(-l2,mid+1))
        a[mid]=i
 
        i+=1
    print(*a)
 