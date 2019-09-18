#https://www.codechef.com/FLMOCK02/problems/CIELRCPT

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass



t=int(input()) 
while t!=0:
    t-=1
    amount=int(input())
    coin=1
    while coin<=amount:
        coin=coin*2
    if(coin>amount):
        coin=coin//2
    if(coin>2048):
        coin=2048
    limit=coin
    dp=[float("inf") for i in range(amount+1)]
    dp[0]=0
    coins=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    coin_list=[]
    for c in coins:
        if(c<=limit):
            coin_list.append(c)
    for c in coin_list:
        for i in range(1,amount+1):
            if(c<=i):
                dp[i]=min(1+dp[i-c],dp[i])

    print(dp[amount])




