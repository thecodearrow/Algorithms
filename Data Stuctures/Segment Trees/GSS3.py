#https://www.spoj.com/problems/GSS3/

n=int(input())
a=[int(x) for x in input().split()]
q=int(input())

from collections import defaultdict

class Node:
	def __init__(self):
		#setting up values to negative infinity

		self.max_subarray_sum=-10**7
		self.max_prefix_sum=-10**7
		self.max_suffix_sum=-10**7
		self.total_sum=-10**7

seg_tree=defaultdict(Node)


def mergeValues(left,right): 
	#merging left child and right child values
	parent=Node()
	parent.total_sum=left.total_sum+right.total_sum
	parent.max_prefix_sum=max(left.max_prefix_sum,left.total_sum+right.max_prefix_sum)
	parent.max_suffix_sum=max(left.max_suffix_sum+right.total_sum,right.max_suffix_sum)
	parent.max_subarray_sum=max(left.max_subarray_sum,right.max_subarray_sum,left.max_suffix_sum+right.max_prefix_sum)
	return parent 


def buildTree(a,start,end,pos):
	if(start==end):
		ele=a[start]
		seg_tree[pos].max_subarray_sum=ele
		seg_tree[pos].max_prefix_sum=ele
		seg_tree[pos].max_suffix_sum=ele
		seg_tree[pos].total_sum=ele
		return seg_tree[pos]
	mid=(start+end)//2
	leftchild=buildTree(a,start,mid,2*pos+1)
	rightchild=buildTree(a,mid+1,end,2*pos+2)
	seg_tree[pos]=mergeValues(leftchild,rightchild)
	return seg_tree[pos]


def findAns(L,R,start,end,pos):
	if(L>end or R<start): #no overlap
		return Node() #null
	if(start>=L and end<=R): #complete overlap
		return seg_tree[pos]
	mid=(start+end)//2
	l=findAns(L,R,start,mid,2*pos+1)
	r=findAns(L,R,mid+1,end,2*pos+2)
	ans=mergeValues(l,r)
	return ans


def pointUpdate(start,end,pos,index,ele):
	if(index<start or index>end): #no overlap
		return 
	if(start==end): #leaf node
		#update node
		a[index]=ele
		seg_tree[pos].max_subarray_sum=ele
		seg_tree[pos].max_prefix_sum=ele
		seg_tree[pos].max_suffix_sum=ele
		seg_tree[pos].total_sum=ele
		return 
	mid=(start+end)//2	
	pointUpdate(start,mid,2*pos+1,index,ele)
	pointUpdate(mid+1,end,2*pos+2,index,ele)
	seg_tree[pos]=mergeValues(seg_tree[2*pos+1],seg_tree[2*pos+2])
	return 


buildTree(a,0,n-1,0)
while(q!=0):
	q-=1
	temp=[int(x) for x in input().split()]
	if(temp[0]==0):
		#point update
		idx=temp[1]-1
		e=temp[2]
		pointUpdate(0,n-1,0,idx,e)
	
	
		
	else:
		#query
		qlow=temp[1]-1
		qhigh=temp[2]-1
		ans=findAns(qlow,qhigh,0,n-1,0).max_subarray_sum
		print(ans)


