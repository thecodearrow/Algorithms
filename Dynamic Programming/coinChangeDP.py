import sys

def getWays(n, c):
    # Complete this function
    combinations=[0]*(n+1)
    combinations[0]=1
    
    for coin in c:
        for i in range(n+1):
            if(coin<=i):
                combinations[i]+=combinations[i-coin]
                
    return combinations[n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
