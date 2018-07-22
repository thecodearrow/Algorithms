#http://codeforces.com/contest/510/problem/C

#https://www.quora.com/What-is-the-algorithmic-approach-to-solve-the-Codeforces-problem-Fox-and-Names


#Great problem, tests for cycles and also involves topological sorting


n=int(input())
strings=[]
for i in range(n):
	t=input()
	strings.append(t)

from collections import deque
from collections import defaultdict
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(set)

	def addEdge(self,u,v):
		self.neighbours[u].add(v) 

	def isCyclicVisit(self,u,black_stack,grey_stack):
		grey_stack[u]=True 
		black_stack[u]=True 
		for v in self.neighbours[u]:
			if(not black_stack[v]):
				if(self.isCyclicVisit(v,black_stack,grey_stack)):
					return True
			elif(grey_stack[v]):
				return True
				
			
		grey_stack[u]=False
		return False

	def isCyclic(self,white_stack):
		black_stack=defaultdict(lambda:False)
		grey_stack=defaultdict(lambda:False)
		for w in white_stack:
			grey_stack=defaultdict(lambda:False)
			if(not black_stack[w]):
				if(self.isCyclicVisit(w,black_stack,grey_stack)):
					return True 
		return False
			
	def dfs(self,u,visited,topological_order):
		visited[u]=True
		for v in self.neighbours[u]:
			if(v not in visited):
				self.dfs(v,visited,topological_order)
		
		topological_order.appendleft(u)
	


	def dfs_visit(self,s):
		alphabets=[]
		topological_order=deque()
		visited=defaultdict(lambda:False)
		for i in range(97,123):
			alphabets.append(chr(i))
		for c in alphabets:
			if(c not in visited):
				self.dfs(c,visited,topological_order)
			
		return topological_order 
				
	



g=Graph()


#add edges
leflag=False #careful followed by care is impossible
vertices=[]
for i in range(n-1):
	first=strings[i]
	second=strings[i+1]
	flen=len(first)
	slen=len(second)
	if(flen>slen): #second is a substring of 
		if(first[:slen]==second):
			leflag=True
			break
	for j in range(0,min(flen,slen)):
		if(first[j]!=second[j]):
			vertices.append(first[j])
			#first mismatch
			#MAKE SURE YOU ADD AN 
			g.addEdge(first[j],second[j])
			break 

order=g.dfs_visit('z')

if(leflag or g.isCyclic(vertices)):
	print("Impossible")
else:
	print(''.join(order))



	