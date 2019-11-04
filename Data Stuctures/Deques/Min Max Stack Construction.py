class MinMaxStack:
	def __init__(self):
		self.mainStack=[]
		self.minMaxStack=[] #[min,max] till now! 
	def updateMinMaxStack(self,number):
		l=len(self.minMaxStack)
		if(l==0):
			minElement=maxElement=number
		else:
			minElement,maxElement=self.minMaxStack[-1]
			minElement=min(minElement,number)
			maxElement=max(maxElement,number)
		self.minMaxStack.append((minElement,maxElement))
		
    def peek(self):
        if(self.mainStack):
			topElement=self.mainStack[-1]
			return topElement
	
    def pop(self):
		if(self.mainStack):
			poppedElement=self.mainStack.pop()
			self.minMaxStack.pop()
			return poppedElement

    def push(self, number):
		self.updateMinMaxStack(number)
		self.mainStack.append(number)

    def getMin(self):
		if(self.mainStack):
			minElement,maxElement=self.minMaxStack[-1]
			return minElement


    def getMax(self):
		if(self.mainStack):
			minElement,maxElement=self.minMaxStack[-1]
			return maxElement
