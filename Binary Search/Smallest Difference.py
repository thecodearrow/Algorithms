def smallestDifference(arrayOne, arrayTwo):
	a=sorted(arrayOne)
	b=sorted(arrayTwo)
	answer=[None, None]
	na=len(a)
	nb=len(b)
	current_diff=float("inf")
	#O(NA Log(NB))
	for ele in a:
		low=0
		high=nb-1
		while low<=high:
			mid=(low+high)//2
			if(abs(b[mid]-ele)<current_diff):
				answer=[ele,b[mid]]
				if(answer[0]==answer[1]):
					return answer
				current_diff=abs(b[mid]-ele)
			if(b[mid]>ele):
				high=mid-1
			else:
				low=mid+1
			
		
	return answer