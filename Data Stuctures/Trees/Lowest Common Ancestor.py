#https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

#https://www.youtube.com/watch?v=TIoCCStdiFo&index=16&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu

class Tree:
	def __init__(self,value):
		self.data=value
		self.left=None
		self.right=None 

	def insertBST(self,value):
		if(value<self.data):
			if(self.left is not None):
				self.left.insertBST(value)
			else:
				self.left=Tree(value)
		else:
			if(self.right is not None):
				self.right.insertBST(value)
			else:
				self.right=Tree(value)


	def LCA(self,v1,v2):
		if(v1<self.data and v2<self.data):
			#move leftwards
			self.left.LCA(v1,v2)
		elif(v1>self.data and v2>self.data):
			#move rightwards
			self.right.LCA(v1,v2)
		else:
			return self.data #LCA 


t=Tree(4)
t.insertBST(2)
t.insertBST(3)
t.insertBST(1)
t.insertBST(7)
t.insertBST(6)

print(t.LCA(1,7))


			
