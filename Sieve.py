import math
from collections import defaultdict
prime={}

n=int(input())
for i in range(2,n+1):
	prime[i]=True #assuming every number is prime

s=int(math.sqrt(n))

for i in range(2,s+1):
	if(prime[i]):
		for j in range(2*i,n+1,i):
			prime[j]=False #canceling out all multiples of i

for p in range(2,n+1):
	if(prime[p]):
		print(p,end=" ")