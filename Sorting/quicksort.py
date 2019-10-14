a=[10,9,8,7,6,5,4,3,2,1]

def quickSort(start,end):
	if(start<end): #atleast two elements are present
		pIndex=partition(start,end)
		quickSort(start,pIndex-1)
		quickSort(pIndex+1,end)

def partition(start,end):
	pivot=a[end] #choose pivot
	wall=start 
	for i in range(start,end+1):
		if(a[i]<pivot):
			a[wall],a[i]=a[i],a[wall]
			wall+=1


	#swap pivot and wall
	a[end],a[wall]=a[wall],a[end]
	return wall 

quickSort(0,9)
print(a)