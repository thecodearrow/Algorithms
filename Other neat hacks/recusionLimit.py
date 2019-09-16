#In case TopDown DP gives you a Run Time Error

#Either convert it to Bottom up 

#or 


#https://www.codechef.com/SEPT19B/problems/GDSUB/




sys.setrecursionlimit(10**6) #Increase Recursion Limit
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


\










