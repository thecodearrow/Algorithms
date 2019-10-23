def bubbleSort(a):
	n=len(a)
	for i in range(n):
		for j in range(1,n-i):
			if(a[j]<a[j-1]):
				a[j-1],a[j]=a[j],a[j-1]
				
	return a
