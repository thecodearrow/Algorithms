#https://www.codechef.com/ADMOCK01/problems/MINEAT

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


def canEatBananas(bananas,givenHours,eatingRate):
    h=0
    for b in bananas:
        h+=(math.ceil(b/eatingRate))
    if(h<=givenHours):
        return True
    else:
        return False



t=int(input())
while t!=0:
    t-=1
    n,h=[int(x) for x in input().split()]
    bananas=[int(x) for x in input().split()]
    low=1
    high=max(bananas)
    while low<high:
        mid=(low+high)//2
        if(canEatBananas(bananas,h,mid)):
            high=mid
        else:
            low=mid+1

    print(high)


