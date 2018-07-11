#https://www.spoj.com/problems/FREQUENT/
"""
One solution--

#https://w84iit.wordpress.com/2017/06/14/first-blog-post/

Test Cases--

http://spojtoolkit.com/history/FREQUENT


"""

import psyco
psyco.full()

from collections import defaultdict
freq=defaultdict(lambda:0)

class Node:
	def __init__(self):
		self.prefixval=0
		self.prefixcount=0
		self.suffixval=0
		self.suffixcount=0
		self.best=0


def mergeValues(left,right):
	parent=Node()
	parent.prefixval=left.prefixval 
	parent.prefixcount=left.prefixcount
	parent.suffixval=right.suffixval
	parent.suffixcount=right.suffixcount
	parent.best=max(left.best,right.best)
	#3 cases
	if(left.prefixval==right.prefixval):
		parent.prefixcount=left.prefixcount+right.prefixcount 
	if(left.suffixval==right.suffixval):
		parent.suffixcount=left.suffixcount+right.suffixcount
	if(left.suffixval==right.prefixval):
		parent.best=max(parent.best,left.suffixcount+right.prefixcount)
	return parent 

def buildTree(a,seg_tree,start,end,pos):
	if(start==end):
		seg_tree[pos]=Node()
		seg_tree[pos].prefixval=a[start]
		seg_tree[pos].suffixval=a[start]
		seg_tree[pos].prefixcount=1
		seg_tree[pos].suffixcount=1 
		seg_tree[pos].best=1 
		return seg_tree[pos]

	mid=(start+end)//2
	l=buildTree(a,seg_tree,start,mid,2*pos+1)
	r=buildTree(a,seg_tree,mid+1,end,2*pos+2)
	seg_tree[pos]=mergeValues(l,r)
	return seg_tree[pos]


def findAns(a,seg_tree,L,R,start,end,pos):
	if(L<=start and end<=R):
		return seg_tree[pos]
	if(start>R or end<L):
		return Node()
	mid=(start+end)//2
	l=findAns(a,seg_tree,L,R,start,mid,2*pos+1)
	r=findAns(a,seg_tree,L,R,mid+1,end,2*pos+2)
	return mergeValues(l,r)

n,q=[int(x) for x in raw_input().split()]
a=[int(x) for x in raw_input().split()]
seg_tree=[0 for i in range(4*n)]
buildTree(a,seg_tree,0,n-1,0)
t=[int(x) for x in raw_input().split()]
while(t[0]!=0):
	L=t[0]-1
	R=t[1]-1
	t=[int(x) for x in raw_input().split()]
	print(findAns(a,seg_tree,L,R,0,n-1,0).best)