

#https://www.spoj.com/problems/GSS1/

#https://www.geeksforgeeks.org/maximum-subarray-sum-given-range/
from collections import defaultdict

class Node:
	def __init__(self):
		#setting up values to negative infinity

		self.max_subarray_sum=-10**7
		self.max_prefix_sum=-10**7
		self.max_suffix_sum=-10**7
		self.total_sum=-10**7

n=int(raw_input())
a=[int(x) for x in raw_input().split()]
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






buildTree(a,0,n-1,0)
q=int(raw_input())

while q!=0:
	q-=1
	qlow,qhigh=[int(x) for x in raw_input().split()]
	qlow-=1
	qhigh-=1
	ans=findAns(qlow,qhigh,0,n-1,0).max_subarray_sum
	print(ans)
