#Codeforces 455A

from collections import defaultdict
n=int(input())

a=[int(z) for z in input().split()]

maximum=max(a) #max element in a 

freq={} #stores the frequency of each element 
freq=defaultdict(lambda:0,freq)

for ele in a:
    freq[ele]+=1    

dp=[0]*(maximum+1) #dp[n] gives the maxium possible value upto n 

dp[0]=0
dp[1]=freq[1]

for i in range(2,maximum+1):
    dp[i]=max(dp[i-1],freq[i]*i+dp[i-2]) #either selecting i or dropping it

print(dp[maximum])
