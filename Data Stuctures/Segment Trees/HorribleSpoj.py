#Good problem on Lazy Propagation

#https://www.spoj.com/problems/HORRIBLE/

#AC using PyPy :)


t=int(input())
while t!=0:
	t-=1
	n,c=[int(x) for x in input().split()]
	a=[0 for i in range(n)]
	seg_tree=[0 for i in range(4*n)]
	lazy=[0 for i in range(4*n)]
	def buildTree(start,end,pos):
		if(start==end):
			seg_tree[pos]=a[start]
			return a[start]
		mid=(start+end)//2
		l=buildTree(start,mid,2*pos+1)
		r=buildTree(mid+1,end,2*pos+2)
		seg_tree[pos]=l+r
		return (l+r)

	def rangeUpdate(L,R,start,end,pos,value):
		if(lazy[pos]!=0):
			seg_tree[pos]+=(end-start+1)*lazy[pos]
			if(start!=end):
				lazy[2*pos+1]+=lazy[pos]
				lazy[2*pos+2]+=lazy[pos]
			lazy[pos]=0 
		if(end<L or start>R):
			return 
		if(start>=L and end<=R):
			seg_tree[pos]+=(end-start+1)*value
			if(start!=end):
				lazy[2*pos+1]+=value
				lazy[2*pos+2]+=value 
			return 
		mid=(start+end)//2
		rangeUpdate(L,R,start,mid,2*pos+1,value)
		rangeUpdate(L,R,mid+1,end,2*pos+2,value)
		seg_tree[pos]=seg_tree[2*pos+1]+seg_tree[2*pos+2]
		
	def printSumQuery(L,R,start,end,pos):
		if(lazy[pos]!=0):
			seg_tree[pos]+=(end-start+1)*lazy[pos]
			if(start!=end):
				lazy[2*pos+1]+=lazy[pos]
				lazy[2*pos+2]+=lazy[pos]
			lazy[pos]=0 
		if(end<L or start>R):
			return 0
		if(start>=L and end<=R):
			return seg_tree[pos]

		mid=(start+end)//2
		l=printSumQuery(L,R,start,mid,2*pos+1)
		r=printSumQuery(L,R,mid+1,end,2*pos+2)
		return l+r

	buildTree(0,n-1,0)
	while c!=0:
		c-=1
		temp=[int(x) for x in input().split()]
		if(temp[0]==0):
			p=temp[1]-1
			q=temp[2]-1
			v=temp[3]
			rangeUpdate(p,q,0,n-1,0,v)
		else:
			p=temp[1]-1
			q=temp[2]-1
			print(printSumQuery(p,q,0,n-1,0))


