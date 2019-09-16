# https://www.codechef.com/FLPAST01/problems/BADMATH/
from collections import defaultdict
t=int(input())
def numWays(i,s,n,m):
    if(i>=n):
        if(int(s,2)%m==0):
            return 1
        else:
            return 0
    if(s[i]=="_"):
        s1=s[:i]+"0"+s[i+1:]
        s2=s[:i]+"1"+s[i+1:]
        return numWays(i+1,s1,n,m)+numWays(i+1,s2,n,m)
    else:
        return numWays(i+1,s,n,m)

while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    s=input()
    print(numWays(0,s,n,m))

