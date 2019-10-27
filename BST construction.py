class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if(self is None):
            newNode=BST(value)
            self=newNode
        else:
            node=self
            insertedNode=False
            while not insertedNode:
                if(value<node.value):
                    if(node.left):
                        node=node.left
                    else:
                        newNode=BST(value)
                        node.left=newNode
                        insertedNode=True
                else:
                    if(node.right):
                        node=node.right
                    else:
                        newNode=BST(value)
                        node.right=newNode
                        insertedNode=True

        return self

    def contains(self, value):
        # Write your code here.
        node=self
        while node is not None:
            if(node.value==value):
                return True
            elif(value<node.value):
                node=node.left
            else:
                node=node.right
                
        return False
    
    def findNode(self,value):
        node=self
        parentNode=node
        while node!=None and node.value!=value:
            parentNode=node
            if(value<node.value):
                node=node.left
            else:
                node=node.right
                
        return node
    def findMinNode(self,node):
        #Finding min node in right sub tree
        while node.left:
            node=node.left
        return node
        
    

    #Code is much simpler in C++ 
    #https://www.youtube.com/watch?v=gcULXE7ViZw&t=920s
    #No need to maintain parent pointer
    def remove(self, value, parentNode=None):
        currentNode=self
        if(value<self.value):
            if(self.left):
                self.left.remove(value,self)
        elif(value>self.value):
            if(self.right):
                self.right.remove(value,self)
        else:
            #Found the node, time to delete it
            # Node has 2 children
            if(self.left is not None and self.right is not None):
                to_replace_node=self.findMinNode(self.right)
                self.value=to_replace_node.value
                self.right.remove(to_replace_node.value,self)
            elif(parentNode is None):
                #Root Node is the node to be deleted
                if(self.left is None):
                    self=self.right
                elif(self.right is None):
                    self=self.left
                else:
                    #No children root node case
                    self=None
            else:
                if(parentNode.left==self):
                    if(self.left):
                        parentNode.left=self.left
                    else:
                        parentNode.left=self.right


                elif(parentNode.right==self):
                    if(self.left):
                        parentNode.right=self.left
                    else:
                        parentNode.right=self.right

        
        return self

    def printTree(self):
        if(self==None):
            return
        if(self.left):
            self.left.printTree()
        print(self.value,end="->")
        if(self.right):
            self.right.printTree()




b=BST(4)
b.insert(3)
b.insert(2)
b.remove(4).printTree()
