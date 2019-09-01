#https://www.spoj.com/problems/MIXTURES/
#https://www.youtube.com/watch?v=XHjjIJxnAJY

from collections import defaultdict
def getSum(start,end,colors):
    s=0
    for i in range(start,end+1):
        s+=colors[i]
        s=s%100
    return s

def solveMixtures(start,end,dp,colors):
    if(start>=end):
        return 0 #smoke generated from single element is also zero
    key=str(start)+":"+str(end)
    if(dp[key]!=-1):
        return dp[key]
    dp[key]=10**9+7 #INF
    for k in range(start,end+1):
        dp[key]=min(dp[key],solveMixtures(start,k,dp,colors)+solveMixtures(k+1,end,dp,colors)+getSum(start,k,colors)*getSum(k+1,end,colors))

    return dp[key]

while True:
    try:
        n=input()
        if(len(n)>0):
            n=int(n)
        colors=[int(x) for x in input().split()]
        dp=defaultdict(lambda:-1)
        print(solveMixtures(0,n-1,dp,colors))   
    except EOFError:
        break
     

