#!/bin/python3

import math
import os
import random
import re
import sys

def longestCommonSubsequence(a, b):
    common=[]
    l1=len(a)
    l2=len(b)
    dp=[]
    for i in range(l1+1):
        dp.append([])
        for j in range(l2+1):
            dp[i].append(0)
            
            
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if(a[i-1]==b[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            
            else:

                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    
    count=dp[l1][l2]
    i=l1
    j=l2
    common=[]

    #tracking back to find the LCS

    while(i>0):
        if(dp[i][j]==dp[i-1][j]):
            i-=1
        elif(dp[i][j]==dp[i][j-1]):
            j-=1 
        
        elif(dp[i][j]==dp[i-1][j-1]+1):
            common.append(a[i-1])
            i-=1 
            j-=1

        
        

    for c in common[::-1]:
        print(c,end=" ")
        
        
    
                
l1,l2=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
longestCommonSubsequence(a,b)
       

