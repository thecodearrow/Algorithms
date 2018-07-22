#https://www.hackerrank.com/contests/srin-aadc03/challenges/classic-01-knapsack/problem

#we use 2d array because we can only select an item ONCE! 
t=int(input())
for case in range(t):
    s,n=[int(x) for x in input().split()]
    weights=[0]
    values=[0]
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(s+1):
            dp[i].append(0)
    for i in range(n):
        temp=[int(x) for x in input().split()]
        weights.append(temp[0])
        values.append(temp[1])

    for j in range(1,n+1):
        w=weights[j]
        v=values[j]
        for i in range(1,s+1):
            if(i>=w):
                dp[j][i]=max(dp[j-1][i],v+dp[j-1][i-w])
            else:
                dp[j][i]=dp[j-1][i]
               
        
    print(dp[n][s])
    