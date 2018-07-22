class Tree:
	def __init__(self,data):
		self.data=data 
		self.left=None
		self.right=None

	def insert(self,value):
		if value<self.data:
			if self.left is None:
				self.left=Tree(value)
			else:
				self.left.insert(value)

		elif value>self.data:
			if self.right is None:
				self.right=Tree(value)
			else:
				self.right.insert(value) 

	def preOrder(self):
		#ele L R
		if(self.data is None ):
			return 
		print(self.data,end=" ")
		if(self.left):
			self.left.preOrder()
		if(self.right):
			self.right.preOrder()

	def InOrder(self):
		#L ele R
		if(self.data is None):
			return 
		if(self.left):
			self.left.InOrder()
		print(self.data,end=" ")
		if(self.right):
			self.right.InOrder()

	def PostOrder(self):
		#L R ele
		if(self.data is None):
			return 
		if(self.left):
			self.left.PostOrder()
		if(self.right):
			self.right.PostOrder()
		print(self.data,end=" ")
		

	def size(self):
		l=0 
		r=0
		if(self.data is None):
			return 0
		if(self.left):
			l=self.left.size()
		if(self.right):
			r=self.right.size()
		return (l+r+1)

	def height(self):
		l=0
		r=0
		if(self.data is None):
			return 0  #return -1 if you don't want to count root
		if(self.left):
			l=self.left.height()
		if(self.right):
			r=self.right.height()
		return max(l,r)+1

	def LevelOrder(self):
		queue=[self]
		while queue:
			ele=queue.pop(0)
			print(ele.data,end=" ")
			if(ele.left):
				queue.append(ele.left)
			if(ele.right):
				queue.append(ele.right)

	

		
				



t=Tree(3)
t.insert(5)
t.insert(2)
t.insert(1)
t.insert(4)
t.insert(6)
t.insert(7)

t.preOrder()
print()
t.InOrder()
print()
t.PostOrder()
print("\nThe size of the tree is ", t.size())
print("\nThe height of the tree is ", t.height())
t.LevelOrder()


