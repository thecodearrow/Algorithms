
#https://www.codechef.com/ADMOCK01/problems/TSHIRTS
#PYPY3 AC

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass



t=int(input())
def countWays(personMask,shirtNum,shirtsMap,n,memo):
    if(personMask==(pow(2,n)-1)):
        #every person has been asigned a shirt
        return 1
    if(shirtNum>100):
        #before the shirts got over, all people couldn't be asigned tshirts
        return 0
    key=str(personMask)+":"+str(shirtNum)
    if(key in memo):
        return memo[key]
    ans=countWays(personMask,shirtNum+1,shirtsMap,n,memo) #not assigning this current shirt
    people=shirtsMap[shirtNum]
    for p in people:
        if(personMask&(1<<p)==0):
            #has not been set
            ans+=countWays(personMask|(1<<p),shirtNum+1,shirtsMap,n,memo)
    memo[key]=ans
    return memo[key]


    

while t!=0:
    t-=1
    shirtsMap=defaultdict(list)
    n=int(input())
    for i in range(n):
        shirts=[int(x) for x in input().split()]
        for s in shirts:
            shirtsMap[s].append(i)

    personMask=0
    memo=[]

    print(countWays(personMask,1,shirtsMap,n,{})%(10**9+7))

