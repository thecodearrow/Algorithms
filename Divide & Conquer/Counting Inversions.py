#https://www.coursera.org/lecture/algorithms-divide-conquer/o-n-log-n-algorithm-for-counting-inversions-i-GFmmJ

#Really amazing to understand how merge sort works! :) 

from collections import defaultdict 

contrib=defaultdict(lambda:0)

def countInversion(arr):
	if(len(arr)==1):
		return arr,0 #no inversions for single element

	mid=len(arr)//2
	a,ai=countInversion(arr[:mid])
	b,bi=countInversion(arr[mid:])
	c=[] #merged array after sorting
	i=0
	j=0
	inversions=ai+bi 

	#calculating split inversions
	while(i<len(a) and j<len(b)):
		if(a[i]<b[j]):
			c.append(a[i])
			contrib[a[i]]+=1
			i+=1 
			inversions+=len(b)-j 
		else:

			c.append(b[j])
			j+=1
			

	#remaining elements 

	c+=a[i:]
	c+=b[j:]
	return c, inversions 
	



print(countInversion("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefz"))
print(dict(contrib))