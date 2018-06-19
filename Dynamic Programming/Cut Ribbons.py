#CodeForces 189A
n,a,b,c=[int(z) for z in input().split()]

ribbons=[a,b,c]

dp=[-10**7+7]*(n+1) 

dp[0]=0

for i in range(1,n+1):
    for r in ribbons:
        if(r<=i):
            dp[i]=max(dp[i],dp[i-r]+1)
 
print(dp[n])