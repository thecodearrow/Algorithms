sum=0
cache={}
MOD=10**9+7
def fib(n):
    #in logn time!
    if(n<2):
        return 1
    if(n in cache):
        return cache[n]
    cache[n]=(fib((n+1) // 2)*fib(n//2) + fib((n-1) // 2)*fib((n-2) // 2)) % MOD
    return cache[n]