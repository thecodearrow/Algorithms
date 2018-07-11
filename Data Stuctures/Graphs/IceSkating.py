"""
http://codeforces.com/contest/217/problem/A

Notice that the existence of a snow drift at the point (x, y) implies that 
"if I'm on the horizontal line at y then I am certainly able to get to the
 vertical line at x, and vice versa".

2
2 1
1 2

"""

from collections import defaultdict
n=int(input())

def DFS(x,y,visited_coords,s):
	visited_coords[s]=True
	for i in range(n):
		if(not visited_coords[i] and (x[s]==x[i] or y[s]==y[i])):
			DFS(x,y,visited_coords,i)

visited_coords=defaultdict(lambda:False,{})
x=[]
y=[]
for i in range(n):
	x1,y1=[int(m) for m in input().split()]
	x.append(x1)
	y.append(y1)

unique_visits=0 

for i in range(n):
	if(not visited_coords[i]):
		DFS(x,y,visited_coords,i)
		unique_visits+=1 

print(unique_visits-1)
