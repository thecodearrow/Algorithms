#https://codeforces.com/contest/1237/problem/B

import math
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
 
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
 
def mergeSortInversions(arr):
    l=len(arr)
    if l == 1:
        return arr
    else:
        a = arr[:l//2]
        b = arr[l//2:]
        a= mergeSortInversions(a)
        b= mergeSortInversions(b)
        c = []
        i = 0
        j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            count[a[i]]+=1 #This is where the magic happens
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            
    c += a[i:]
    c += b[j:]
    return c
 
 
n=int(input())
entry=takeInput()
exit=takeInput()
order={}
index=1
for ele in entry:
    order[ele]=index
    index+=1
 
 
for i in range(n):
    exit[i]=order[exit[i]]
 
 
seen=[False for i in range(n+1)]
fines=0
count=[0 for i in range(n+1)]
mergeSortInversions(exit)
 
for i in range(n+1):
    if(count[i]!=0):
        fines+=1
 
print(fines)
 
