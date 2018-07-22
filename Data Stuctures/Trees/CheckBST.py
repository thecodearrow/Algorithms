#https://www.youtube.com/watch?v=MILxfAbIhrE&index=8&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu

class Tree:
	def __init__(self,data):
		self.data=data 
		self.left=None
		self.right=None



	def checkBST(self,range):
			l=True
			r=True
			if(self.data is None):
				return True
			if(self.data>range[0] and self.data<range[1]):
				if(self.left):
					l=self.left.checkBST([range[0],self.data])
				if(self.right):
					r=self.right.checkBST([self.data,range[1]])

				return l and r 
			else:
				return False



t=Tree(10)
t.left=Tree(0)
t.right=Tree(25)
t.left.left=Tree(-1)
t.left.right=Tree(21) #violates BST
print(t.checkBST([-10**9,10**9])) #initial range -inf to +inf