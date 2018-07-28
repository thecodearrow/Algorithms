#Queries for counts of array elements with values in given range 
import bisect
#bisect.bisect_right(a,ele) can be used

def binSearchInsertLeft(a,ele,low,high):
	#bisect.bisect_left(a,ele) can be used
	while low<=high:
		mid=(low+high)//2
		if ele<=a[mid]:
			high=mid-1
		else:
			low=mid+1
		
	return low

def binSearchInsertRight(a,ele,low,high):
	#bisect.bisect_right(a,ele) can be used
	while low<=high:
		mid=(low+high)//2
		if a[mid]<=ele:
			low=mid+1
		else:
			high=mid-1
	return low


a=[10,20,30,40,50,60,70,80]
n=len(a)
a=sorted(a)
q=int(input())
exists={} 
for ele in a:
	exists[ele]=True
for i in range(q):
	count=0
	l,r=[int(x) for x in input().split()]
	left=binSearchInsertLeft(a,l,0,n-1)
	right=binSearchInsertRight(a,r,0,n-1)
	left1=bisect.bisect_left(a,l)
	right1=bisect.bisect_right(a,r)
	count=right-left 
	count2=right1-left1
	print(left,right,count,"By implementation")
	print(left1,right1,count2,"By using bisect_left and bisect_right")
