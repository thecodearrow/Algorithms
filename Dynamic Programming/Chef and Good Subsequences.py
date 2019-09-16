#https://www.codechef.com/SEPT19B/problems/GDSUB/


import sys
import math
from collections import defaultdict
from collections import Counter
from itertools import combinations
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

sys.setrecursionlimit(2500)
def countWays(n,k,f,memo):
    key=str(n)+":"+str(k)
    if(key in memo):
        return memo[key]
    if(k==-1):
        return 1
    if(n==-1):
        return 1
    else:
        memo[key]=(f[n]*countWays(n-1,k-1,f,memo))+countWays(n-1,k,f,memo)
        return memo[key]



n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
modulo=10**9+7
frequencies=[]
primes=list(set(a))
count=Counter(a)
for p in primes:
    frequencies.append(count[p])


ans=(countWays(len(frequencies)-1,k-1,frequencies,{}))
ans=ans%modulo 
print(ans)










    