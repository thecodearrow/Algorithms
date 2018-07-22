"""

On a field represented as a matrix of N rows and M columns there is a santa and two presents.

Santa has one child pending to give a gift to and wants to get to a gift as fast as possible. He can walk in four directions: up, down, left or right. The indecisiveness of the Santa is that if the two gifts are equally close to him he won't be able to decide which one to choose and he will end up not gifting the child at all.

You are given the cells of the gifts, but you don't know where Santa is. Compute the number of cells where Santa will become indecisive if he's there.

INPUT

The first line contains the two integers N and M.(2 ≤ N,M ≤ 200)
The second line contains two integers representing the row and the column of the first gift.
The third line contains two integers representing the row and the column of the second gift.
The two gifts and Santa are guaranteed to be in three different cells.
Santa always takes the shortest route to get to a gift.

OUTPUT

Output a single number representing the number of cells where Santa becomes indecisive if he's there. Constraints and notes

Sample Input 0

5 5
2 4
5 3
Sample Output 0

5
Explanation 0

Santa becomes indecisive if he is one of these cells:

(3,1)
(3,2)
(3,3)
(4,4)
(4,5)

"""

#Is there a better solution to this? 14th July 2018

from collections import defaultdict

class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v):
		self.neighbours[u].append(v) 
		self.neighbours[v].append(u)

	def BFS(self,s,gift1,gift2):
		visited=defaultdict(lambda:False)
		dist={s:0}
		visited[s]=True 
		q=[s]
		while q:
			u=q.pop(0)
			if(visited[gift1]==True and visited[gift2]==True):
				if(dist[gift1]==dist[gift2]):
					return True 
				else:
					return False
			for v in self.neighbours[u]:
				if(visited[v]==False):
					visited[v]=True 
					dist[v]=dist[u]+1
					q.append(v)




n,m=[int(x) for x in input().split()]
i1,j1=[int(x) for x in input().split()]
i2,j2=[int(x) for x in input().split()]
gift1=(i1,j1)
gift2=(i2,j2)
g=Graph()
for i in range(1,n+1):
	for j in range(1,m+1):
		g.addEdge((i,j),(i+1,j))
		g.addEdge((i,j),(i,j+1))

count=0
for i in range(1,n+1):
	for j in range(1,m+1):
		if(g.BFS((i,j),gift1,gift2)):
			count+=1

print(count)
