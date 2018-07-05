
def buildTree(a,seg_tree,low,high,pos):
	if(low==high): #base case
		seg_tree[pos]=a[low]
		return seg_tree[pos] 

	mid=(low+high)//2
	l=buildTree(a,seg_tree,low,mid,2*pos+1)
	r=buildTree(a,seg_tree,mid+1,high,2*pos+2)
	seg_tree[pos]=max(l,r)
	return seg_tree[pos]

def findAns(seg_tree,qlow,qhigh,low,high,pos):
	
	if(qlow<=low and high<=qhigh): #Total Overlap
		return seg_tree[pos]
	if(qlow>high or qhigh<low): #No Overlap
		return -(10**7) #negative infinity

	#Partial Overlap 
	mid=(low+high)//2
	l=findAns(seg_tree,qlow,qhigh,low,mid,2*pos+1)
	r=findAns(seg_tree,qlow,qhigh,mid+1,high,2*pos+2)
	return (max(l,r)) 



n=int(input())
a=[int(x) for x in input().split()]
seg_tree=[0]*(4*n)
buildTree(a,seg_tree,0,n-1,0)
q=int(input())

while q!=0:
	q-=1
	qlow,qhigh=[int(x) for x in input().split()]
	qlow-=1
	qhigh-=1
	print(findAns(seg_tree,qlow,qhigh,0,n-1,0))
