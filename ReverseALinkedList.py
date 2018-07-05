class Node:
	def __init__(self,val):
		self.data=val
		self.link=None

	def print(self,head):
		temp=head 
		while(temp!=None):
			print(temp.data,end="->")
			temp=temp.link

	#Recursive approach! 
	def printReverse(self,head):
		if(head==None):
			return 
		self.printReverse(head.link)
		print(head.data,end="->")


	#Iterative approach
	def printRIterative(self,head):
		prev=None 
		current=head 
		while(current!=None):
			next=current.link
			current.link=prev 
			prev=current 
			current=next 

		head=prev
		self.print(head)



n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.link=n2 
n2.link=n3 

n1.print(n1)
print() #newline
n1.printReverse(n1)
print() #newline
n1.printRIterative(n1)