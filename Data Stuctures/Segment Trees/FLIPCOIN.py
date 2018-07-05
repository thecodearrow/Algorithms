#https://www.codechef.com/problems/FLIPCOIN

#Segment Tree with Lazy Propagation! :D

"""
4 7
1 0 3
0 1 2
1 0 1
1 0 0
0 0 3
1 0 3 
1 3 3

"""
def buildTree(a,seg_tree,start,end,pos):
	if(start==end):
		seg_tree[pos]=a[start]
		return seg_tree[pos]
	mid=(start+end)//2
	l=buildTree(a,seg_tree,start,mid,2*pos+1)
	r=buildTree(a,seg_tree,mid+1,end,2*pos+2)
	seg_tree[pos]=(l+r)
	return seg_tree[pos]

def findHeads(seg_tree,lazy_tree,qstart,qend,start,end,pos):
	#if tree is not upto date
	 
	if(lazy_tree[pos]==1):
		
		seg_tree[pos]=(end-start+1)-seg_tree[pos] #total-current_heads=flip
		
		#propagating the lazy tree further

		if(start!=end): #ensuring it's not a leaf node since it will have no children
			lazy_tree[2*pos+1]=1-lazy_tree[2*pos+1]
			lazy_tree[2*pos+2]=1-lazy_tree[2*pos+2]

		lazy_tree[pos]=0
	if(qstart>end or qend<start): #no overlap
		return 0 
		
	if(start>=qstart and end<=qend): #complete overlap
		return seg_tree[pos]
	
	#partial overlap
	mid=(start+end)//2
	l=findHeads(seg_tree,lazy_tree,qstart,qend,start,mid,2*pos+1)
	r=findHeads(seg_tree,lazy_tree,qstart,qend,mid+1,end,2*pos+2)
	return (l+r)

def rangeFlip(seg_tree,lazy_tree,qstart,qend,start,end,pos):
	#if tree is not upto date

	if(lazy_tree[pos]==1):
		
		seg_tree[pos]=(end-start+1)-seg_tree[pos] #total-current_heads=flip
		
		#propagating the lazy tree further

		if(start!=end): #ensuring it's not a leaf node since it will have no children
			lazy_tree[2*pos+1]=1-lazy_tree[2*pos+1]
			lazy_tree[2*pos+2]=1-lazy_tree[2*pos+2]

		lazy_tree[pos]=0


	if(qstart>end or qend<start): #no overlap
		return 0 

	

	"""
	Flipping all leaves is too slow :(
	if(start==end): #update leaves
		seg_tree[pos]=seg_tree[pos]^1 #flipping value
		return seg_tree[pos]
	"""

	
	if(start>=qstart and end<=qend): #complete overlap
		#Calculate total number of coins
		seg_tree[pos]=(end-start+1)-seg_tree[pos] #total-current_heads=flip
		if(start!=end): #marking the lazy tree children that we have changed!
			lazy_tree[2*pos+1]=1-lazy_tree[2*pos+1]
			lazy_tree[2*pos+2]=1-lazy_tree[2*pos+2]

		return 

	mid=(start+end)//2
	rangeFlip(seg_tree,lazy_tree,qstart,qend,start,mid,2*pos+1)
	rangeFlip(seg_tree,lazy_tree,qstart,qend,mid+1,end,2*pos+2)
	seg_tree[pos]=seg_tree[2*pos+1]+seg_tree[2*pos+2]
	



n,q=[int(x) for x in input().split()]
coins=[0]*(n)
seg_tree=[0]*(4*n) #MAX SIZE OF SEGMENT TREE
lazy_tree=[0]*(4*n)
buildTree(coins,seg_tree,0,n-1,0)
for i in range(q):
	
	d,qstart,qend=[int(x) for x in input().split()]
	if(d==1):
		print(findHeads(seg_tree,lazy_tree,qstart,qend,0,n-1,0))
	else:
		rangeFlip(seg_tree,lazy_tree,qstart,qend,0,n-1,0)
		

