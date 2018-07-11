#https://www.youtube.com/watch?v=rKQaZuoUR4M&list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j&index=11

#white stack=unvisited nodes
#grey stack=recursive nodes
#black stack=completed nodes

from collections import defaultdict
class Graph:
	def __init__(self):
		self.neighbours=defaultdict(list)

	def addEdge(self,u,v):
		self.neighbours[u].append(v)

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

	def isCyclic(self,s):
		white_stack=[0,1,2,3]
		black_stack=defaultdict(lambda:False)
		grey_stack=defaultdict(lambda:False)
		for w in white_stack:
			grey_stack=defaultdict(lambda:False)
			if(not black_stack[w]):
				if(self.isCyclicVisit(w,black_stack,grey_stack)):
					return True 
		return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
"""
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

"""
status=g.isCyclic(0)
if(status):
	print("The graph contains cycles.")
else:
	print("The graph is acyclic")



