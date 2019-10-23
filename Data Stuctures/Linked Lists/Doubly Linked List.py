
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
		if(self.head is None):
			self.head=node
			self.tail=node
		else:
			self.insertBefore(self.head,node)

    def setTail(self, node):
        # Write your code here.
		if(self.tail is None):
			self.setHead(node)
		else:
			self.insertAfter(self.tail,node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
		if(node is None or nodeToInsert is None):
			return
		self.remove(nodeToInsert)
		nodeToInsert.next=node
		nodeToInsert.prev=node.prev
		if(node.prev is None):
			self.head=nodeToInsert
		else:
			node.prev.next=nodeToInsert
		node.prev=nodeToInsert
	
		

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		if(node is None or nodeToInsert is None):
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev=node
		nodeToInsert.next=node.next
		if(node.next is None):
			self.tail=nodeToInsert
		else:
			node.next.prev=nodeToInsert
		node.next=nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        currentNode=self.head
        if(position<1 or nodeToInsert is None):
            return
        pos=1
        while currentNode!=None and pos!=position:
            currentNode=currentNode.next
            pos+=1
        
        if(currentNode==None):
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(currentNode,nodeToInsert)

    def removeNodesWithValue(self, value):
        node_iterator=self.head
        while node_iterator!=None:
            currentNode=node_iterator
            node_iterator=node_iterator.next
            if(currentNode.value==value):
                self.remove(currentNode)
            

    def remove(self, node):
        # Write your code here.
		if(node is None):
			return node
		if(node==self.head):
			self.head=self.head.next
		if(node==self.tail):
			#It's not elif so as to handle a single node edge case
			self.tail=self.tail.prev
		if(node.prev):
			node.prev.next=node.next
		if(node.next):
			node.next.prev=node.prev
		#Remove bindings of current node so it can be freed
		node.prev=None
		node.next=None
		

    def containsNodeWithValue(self, value):
        currentNode=self.head
        while currentNode!=None:
            if(currentNode.value==value):
                return True
            currentNode=currentNode.next
            
        return False
