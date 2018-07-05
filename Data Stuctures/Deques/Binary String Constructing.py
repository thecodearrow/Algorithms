#http://codeforces.com/contest/1003/problem/B

zeros,ones,x=[int(x) for x in input().split()]
from collections import deque
a=deque()
count=1

if(x%2!=0):
	times=x 
else:
	times=x-1

for i in range(1,times+1,2):
	a.append('0')
	zeros-=1
	a.append('1')
	ones-=1

if(x%2!=0):
	while(zeros!=0):
		zeros-=1
		a.appendleft('0')


	while(ones!=0):
		ones-=1
		a.append('1')
else:
	if(zeros>0 and ones==0): 
		while(zeros!=0):
			zeros-=1
			a.append('0')
	elif(ones>0 and zeros==0):

		while(ones!=0):
			ones-=1
			a.appendleft('1')
	elif(ones>0 and zeros>0): #can't fill both sides!

		while(ones!=0):
			ones-=1
			a.append('1')
		while(zeros!=0):
			zeros-=1
			a.append('0')



ans=""

for i in a:
	ans+=i 

print(ans)
