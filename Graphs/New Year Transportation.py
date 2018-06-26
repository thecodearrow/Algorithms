
"""
8 4
1 2 1 2 1 2 1
"""

#Directed graph so you can use DFS too!


n,t=[int(x) for x in input().split()]
cell=[int(x) for x in input().split()]
cell.insert(0,0) #cell[0] 
visited=set()

current=1
#http://codeforces.com/problemset/problem/500/A
possible=False 

while(current not in visited):
	if(current==t):
		possible=True 
		break 
	visited.add(current)
	if(current<n):
		current+=cell[current]

if(possible):
	print("YES")
else:
	print("NO")