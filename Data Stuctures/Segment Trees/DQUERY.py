#https://www.spoj.com/problems/DQUERY/
#HINT https://stackoverflow.com/questions/18553567/difficulty-in-understanding-the-approach-for-solving-spoj-dquery
"""
SEGMENT TREE APPROACH

Watch Segment Tree tutorial by Tushar Roy :)


"""

#DOES NOT WORK ATM :( #Need to modify buildTree

distint=set()

def buildTree(a,seg_tree,low,high,pos):
	if(low==high): #base case
		ele=a[low]
		if(ele not in distint):
			distint.add(ele)
			seg_tree[pos]=1
		else:
			seg_tree[pos]=0
		return seg_tree[pos]

	mid=(low+high)//2
	l=buildTree(a,seg_tree,low,mid,2*pos+1)
	r=buildTree(a,seg_tree,mid+1,high,2*pos+2)
	seg_tree[pos]=l+r
	return seg_tree[pos]

def findAns(seg_tree,qlow,qhigh,low,high,pos):
	
	if(qlow<=low and high<=qhigh): #Total Overlap
		return seg_tree[pos]
	if(qlow>high or qhigh<low): #No Overlap
		return 0

	#Partial Overlap 
	mid=(low+high)//2
	l=findAns(seg_tree,qlow,qhigh,low,mid,2*pos+1)
	r=findAns(seg_tree,qlow,qhigh,mid+1,high,2*pos+2)
	return (l+r) 



n=int(input())
a=[int(x) for x in input().split()]
seg_tree=[0]*(2*n-1)
buildTree(a,seg_tree,0,n-1,0)
q=int(input())


while q!=0:
	q-=1
	qlow,qhigh=[int(x) for x in input().split()]
	qlow-=1
	qhigh-=1
	print(findAns(seg_tree,qlow,qhigh,0,n-1,0))
