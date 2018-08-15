"""
#https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0

MATHEMATICAL WAY OF SOLVING THIS  #WORKS ONLY FOR 2 eggs ! ;) 


https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/

Let us make our first attempt on x'th floor. 

 x + (x-1) + (x-2) + (x-3) + .... + 1  = 100

 x(x+1)/2  = 100
         x = 13.651

Therefore, we start trying from 14'th floor. If Egg breaks
we one by one try remaining 13 floors.  If egg doesn't break
we go to 27th floor.
If egg breaks on 27'th floor, we try floors form 15 to 26.
If egg doesn't break on 27'th floor, we go to 39'th floor.

An so on...

"""
import math 
floors=100
eggs=2

#x^2+x-(2*floor)=0 quadratic equation

x=(-1+(math.sqrt(1+4*2*floors)))/2
x=math.ceil(x)


print(x)


#This can also be solved using Bottom Up Dynamic Programming in O(K*N^2) ! => https://www.youtube.com/watch?v=3hcaVyX00_4

#Turns out you can do better = > https://leetcode.com/contest/weekly-contest-97/problems/super-egg-drop/


t=int(input())

while t!=0:
    t-=1
    k,n=[int(x) for x in input().split()] #n floors k eggs
    dp=[]
    
    for i in range(k+1):
        dp.append([])
        for j in range(n+1):
            dp[i].append(0)
            
    for i in range(n+1):
        dp[1][i]=i   #1 egg case
        
        
    for e in range(2,k+1):
        for f in range(1,n+1):
            if(f>=e):
                minimum=10**9+7
                for x in range(1,f+1):
                    current=max(dp[e-1][x-1],dp[e][f-x])+1
                    minimum=min(minimum,current)
            
                dp[e][f]=minimum
            else:
                dp[e][f]=dp[e-1][f]
        
            
    print(dp[k][n])   
        

