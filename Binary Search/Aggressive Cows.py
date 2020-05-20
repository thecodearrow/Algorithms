"""
Farmer John has built a new long barn, with N stalls.
Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows. His cows don't like this barn layout and become aggressive towards each other once put into a stall. 
To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

"""

#https://www.spoj.com/problems/AGGRCOW/

import sys
import math
from collections import Counter,defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    

t=int(input())
def canCowDistance(A,n,cows,dist):
        #Greedily assign cows and see if distance>=dist can be maintained!
        prev_cow=A[0] #put the first cow at the beginning
        cows_assigned=1
        for i in range(1,n):
            current_dist=A[i]-prev_cow
            if(current_dist>=dist):
                prev_cow=A[i] #put cow here!
                cows_assigned+=1
                if(cows_assigned==cows):
                    break
        
        if(cows_assigned>=cows):
            return True  
while t!=0:
    t-=1
    n,cows=takeInput()
    stall=[]
    for i in range(n):
        d=int(input())
        stall.append(d)


    stall=sorted(stall)
    start=1
    end=stall[-1]-stall[0] #max distance possible is at the ends
    max_distance=1
    while start<=end:
        mid=(start+end)//2
        if(canCowDistance(stall,n,cows,mid)):
            max_distance=max(mid,max_distance)
            #try to increase it a little more
            start=mid+1
        else:
            end=mid-1
    
    print(max_distance)


    



        
