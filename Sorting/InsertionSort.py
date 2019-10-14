def insertionSort(array):
	for i in range(1,len(array)):
		currentNum=array[i]
		j=i-1
		while j>=0 and currentNum<array[j]:
			array[j+1]=array[j]
			j-=1
		array[j+1]=currentNum
	
	return array
