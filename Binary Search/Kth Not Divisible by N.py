
#https://codeforces.com/contest/1352/problem/C

"""
You are given two positive integers 𝑛 and 𝑘. Print the 𝑘-th positive integer that is not divisible by 𝑛.

For example, if 𝑛=3, and 𝑘=7, then all numbers that are not divisible by 3 are: 1,2,4,5,7,8,10,11,13…. The 7-th number among them is 10.

"""
import sys
import math

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
    n,k=takeInput()
    if(k>n):
        ans=float("inf")
        rem=k//n
        count=k
        start=k
        end=2*k+1
        while start<=end:
            mid=start+(end-start)//2
            rem=mid-mid//n 
            if(rem>=k):
                ans=mid
                end=mid-1
            if(rem<k):
                start=mid+1
                
        print(ans)
    elif(k==n):
        print(k+1)
    else:
        print(k)





            


        

    
