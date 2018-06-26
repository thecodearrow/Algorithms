#http://codeforces.com/problemset/problem/520/B

#Solving using BFS
from collections import defaultdict
a,b=[int(x) for x in input().split()]
level={a:0}
queue=[a]
visited={}
visited=defaultdict(lambda:False,visited)
visited[a]=True 
count=0
while queue:
	if(b in level):
		print(level[b])
		break 
	parent=queue.pop(0)
	ele1=parent-1
	ele2=parent*2

	if(ele1>0 and not visited[ele1]):
		queue.append(ele1)
		level[ele1]=level[parent]+1
		visited[ele1]=True
		
	if(ele2<=20000 and not visited[ele2]):  #when you're doubling be careful
		queue.append(ele2)
		level[ele2]=level[parent]+1

		
		visited[ele2]=True
		
	
	






















"""
a,b=[int(x) for x in input().split()]
count=0
big=b
small=a
while(big>small):
	count+=1
	if(big%2==0): #even
		big/=2
	else:
		big+=1
ans=count+(small-big)
print(int(ans))

"""