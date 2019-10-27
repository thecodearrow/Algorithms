
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	
    def buildHeap(self, array):
		n=len(array)
		lastParentIndex=self.getMyParentIndex(n)
		heap=array
		for i in range(lastParentIndex,-1,-1):
			self.siftDown(heap,i,n)
			
		return heap

    def siftDown(self,array,index,n):
		left_index=2*index+1
		right_index=2*index+2
		min_element=array[index]
		min_index=index
		if(left_index<n and array[left_index]<min_element):
			min_element=array[left_index]
			min_index=left_index
		if(right_index<n and array[right_index]<min_element):
			min_element=array[right_index]
			min_index=right_index
		#Bubble down
		if(min_index!=index):
			array[index],array[min_index]=array[min_index],array[index]
			self.siftDown(array,min_index,n)
			
		
        

    def siftUp(self,array,currentIndex):
		if(currentIndex!=0):
			parentIndex=self.getMyParentIndex(currentIndex)
			if(array[currentIndex]<array[parentIndex]):
				array[currentIndex],array[parentIndex]=array[parentIndex],array[currentIndex]
				self.siftUp(array,parentIndex)

    def peek(self):
        if(len(self.heap)>0):
			return self.heap[0]

    def remove(self):
    	#Swap the min element with the last_element
		n=len(self.heap)
		self.heap[0],self.heap[n-1],self.heap[n-1],self.heap[0]
		#Pop the min element
		popped=self.heap.pop() 
		#Restore heap
		self.siftDown(self.heap,0,n-1)
		return popped
		
	
	def getMyParentIndex(self,index):
		return (index-1)//2
	
    def insert(self, value):
		#Add it to the end
		self.heap.append(value)
		#Sift upward to restore heap
		n=len(self.heap)
		self.siftUp(self.heap,n-1)
    	
