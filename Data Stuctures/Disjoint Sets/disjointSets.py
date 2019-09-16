#https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/DisjointSet.java


class Node:
	def __init__(self):
		self.data=None
		self.parent=None 
		self.rank=None 

	
class DisjointSet:

	def __init__(self):
		self.datatonode={} # (int data) -> Node() 

	
	def makeSet(self,data):
		current=Node()
		current.data=data
		current.parent=current #pointing to itself
		current.rank=0
		self.datatonode[data]=current #data->Node()

	def union(self,data1,data2):

		node1=self.datatonode[data1]
		node2=self.datatonode[data2]
		data1_repr=self.findSet(node1)
		data2_repr=self.findSet(node2)

		if(data1_repr.data==data2_repr.data):
			return #already in the same set

		r1=data1_repr.rank 
		r2=data2_repr.rank 

		if(r1>r2):
			data2_repr.parent=data1_repr
		elif(r2>r1):
			data1_repr.parent=data2_repr
		elif(r1==r2):
			#increments one of them and any assignment is fine 
			data1_repr.rank+=1
			data2_repr.parent=data1_repr




	def findSet(self,node):
		#Path Compression happens here!
		parent=node.parent
		if(parent.data==node.data):
			return parent 
		node.parent=self.findSet(parent)
		return node.parent 

ds=DisjointSet()

ds.makeSet(1);
ds.makeSet(2);
ds.makeSet(3);
ds.makeSet(4);
ds.makeSet(5);
ds.makeSet(6);
ds.makeSet(7);

ds.union(1, 2);
ds.union(2, 3);
ds.union(4, 5);
ds.union(6, 7);
ds.union(5, 6);
ds.union(3, 7);


for i in range(1,8):
	node=ds.datatonode[i]
	print(ds.findSet(node).data)  


#Alternate and Easier Way!


class DisjointSet():
    def __init__(self,n):
        self.parent=[0]
        self.size=[1]
        self.rank=[0]
        for i in range(1,n+1):
            self.parent.append(i)
            self.size.append(1)
            self.rank.append(0)

    def find(self,node):
    	#doing path compression recursively
        if(node!=self.parent[node]):
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def findIterative(self,node):
        #doing path compression in a non recursive fashion!
        node_copy=node
        while(node!=self.parent[node]):
            node=self.parent[node]
        parent_node=node
        while node_copy!=self.parent[node_copy]:
            next_node=self.parent[node_copy]
            self.parent[node_copy]=parent_node
            node_copy=next_node
        return parent_node

    def union(self,u,v):
        leader_u=self.find(u)
        leader_v=self.find(v)
        if(self.rank[leader_u]>self.rank[leader_v]):
            u,v=v,u
            leader_u,leader_v=leader_v,leader_u
        if(self.rank[leader_u]==self.rank[leader_v]):
            self.rank[leader_v]+=1
        self.parent[leader_u]=leader_v #pointing u to v 
        self.size[leader_v]+=self.size[leader_u]



