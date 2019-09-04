#Time Complexity O(l1*l2)
#Space Complexity O(min(l1,l2)) instead of the standard O(l1*l2)

def levenshteinDistance(str1, str2):
    # Write your code here
	l1=len(str1)
	l2=len(str2)
	if(l1>l2):
		l1,l2=l2,l1
		str1,str2,str2,str1
	prevEditDist=[j for j in range(0,l1+1)]
	currentEditDist=[j for j in range(0,l1+1)]
	
	for i in range(1,l2+1):
		prevEditDist=currentEditDist
		currentEditDist=[j for j in range(0,l1+1)] #init again
		currentEditDist[0]=i
		for j in range(1,l1+1):
			if(str1[j-1]==str2[i-1]):
				currentEditDist[j]=prevEditDist[j-1]
			else:
				currentEditDist[j]=1+min(currentEditDist[j-1],prevEditDist[j-1],prevEditDist[j])
		
	
	return currentEditDist[l1]
			
	