def selectionSort(a):
	n=len(a)
	for i in range(n):
		currentSmallest=a[i]
		smallIndex=i
		for j in range(i+1,n):
			if(a[j]<currentSmallest):
				currentSmallest=a[j]
				smallIndex=j
		a[i],a[smallIndex]=a[smallIndex],a[i]
	
	return a
