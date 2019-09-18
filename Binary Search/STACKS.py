

#https://www.codechef.com/problems/STACKS

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


def findMinStackIndex(stacks,n,ele):
    low=1
    high=n
    if(len(stacks[n-1])==0):
        return -1
    if(ele>=stacks[n-1][-1]):
        return -1 
    while low<high:
        mid=(low+high)//2
        if(ele<stacks[mid][-1]):
            high=mid 
        else:
            low=mid+1
    return high

t=int(input()) 
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    sLength=1
    stacks=defaultdict(list)
    for ele in a:
        minStackIndex=-1
        minStackIndex=findMinStackIndex(stacks,sLength,ele)
        if(minStackIndex!=-1):
            stacks[minStackIndex].pop()
            stacks[minStackIndex].append(ele)
        else:
            stacks[sLength].append(ele)
            sLength+=1

    answer=[sLength-1]
    for idx in range(1,sLength):
        answer.append(stacks[idx][-1])

    print(*answer)




