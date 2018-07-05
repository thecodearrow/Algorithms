#http://codeforces.com/problemset/problem/707/B

"""
5 4 2
1 2 5
1 2 3
2 3 4
1 4 10
1 5

"""
from collections import defaultdict
n,m,k=[int(x) for x in input().split()]
u=[0]
v=[0]
d=[0]
for i in range(m):
	t1,t2,t3=[int(x) for x in input().split()]
	u.append(t1)
	v.append(t2)
	d.append(t3)

flour=defaultdict(lambda:0,{})
if(k>0):
	f=[int(x) for x in input().split()]
	for shop in f:
		flour[shop]=1 

INT_MAX=10**9+7 
ans=INT_MAX
for i in range(1,m+1):
	#flour shop and bakery combo 0,1 or 1,0
	if(flour[u[i]]^flour[v[i]]):
		ans=min(ans,d[i])


if(ans==INT_MAX):
	print(-1)
else:
	print(ans)