#https://www.spoj.com/problems/PPATH/


#Very good application of BFS

#All Primes till 10000 using Sieve of Eratosthenes 

import math
from collections import defaultdict 

prime={}
prime=defaultdict(lambda:False,prime)

n=10000
for i in range(2,n+1):
	prime[i]=True #assuming every number is prime

s=int(math.sqrt(n))

for i in range(2,s+1):
	for j in range(2*i,n+1,i):
		prime[j]=False #canceling out all multiples of i


t=int(input())

while(t!=0):
	t-=1 
	a,b=[int(x) for x in input().split()]
	queue=[a] #source
	visited={}
	visited=defaultdict(lambda:False,visited)
	visited[a]=True 
	level={a:0}
	while(queue):
		val=queue.pop(0)
		value=list(str(val))

		#generate all possible primes varying by one bit of val 
		if(val==b):
			print(level[val])
			break

		for i in range(0,4): 
			for j in range(0,10):
				temp=list(value)
				if(not(i==0 and j==0)): #3 digit numbers ...
					temp[i]=str(j)
					
				temp=''.join(temp)
				temp=int(temp)
				if(prime[temp] and not visited[temp]):
					visited[temp]=True
					queue.append(temp)
					level[temp]=level[val]+1


	




