#https://www.geeksforgeeks.org/check-graphs-cycle-odd-length/

class Graph:
	def __init__(self):
		self.neighbour=defaultdict(list)
		
	def addGear(self,u,v):
		self.nextgear[u].append(v)
		self.nextgear[v].append(u)


	def checkForOddCycles(self,source):
		queue=[source]
		colored=defaultdict(lambda:False,{})
		colored[source]=0
		cycle=False
		
		while(queue):
			u=queue.pop(0)
			for v in self.neighbour[u]:
				if(colored[v]==False):
					colored[v]=colored[u]^1
					queue.append(v)
				elif(colored[v]==colored[u]):
						cycle=True
						break
				