import math
from collections import defaultdict,Counter


N=10**3
limit=int(math.sqrt(N))+1
prime=defaultdict(lambda:True)
spf={}
for i in range(1,N+1):
    spf[i]=i #number itself
for i in range(2,limit):
    if(prime[i]):
        spf[i]=i
        for j in range(i*i,N+1,i):
            prime[j]=False
            if(spf[j]==j):
                #hasn't been marked already
                spf[j]=i
    


#Calculating Prime Factors

N=1000
counter=Counter()
while N!=1:
    counter[spf[N]]+=1
    N=N/spf[N]

print(counter)

#So if N= A**p x B**q x C**r
#No of Factors of N is (p+1).(q+1).(r+1)