"""
http://codeforces.com/problemset/problem/115/A
Calculating the height of the node of a tree basically!

"""

from collections import defaultdict 

n=int(input())
graph={}
graph=defaultdict(lambda:-1,graph)
for i in range(1,n+1):
	ele=int(input())
	graph[i]=ele

depth=0

for i in range(1,n+1):
	count=0
	ele=i
	while(ele!=-1):
		count+=1
		ele=graph[ele]


	depth=max(count,depth)

print(depth)














