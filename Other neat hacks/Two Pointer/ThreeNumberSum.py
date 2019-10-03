#Find all triplets in the array that add up the given sum
#O(N^2 + NLogN) 

#Other alternative is to use Hashing-based approach!

def threeNumberSum(array, targetSum):
	array=sorted(array)
	answers=[]
	n=len(array)
	for i in range(n-2):
		x=array[i]
		left=i+1
		right=n-1
		while left<right:
			y=array[left]
			z=array[right]
			if(x+y+z==targetSum):
				answers.append(sorted([x,y,z]))
			if(x+y+z<targetSum):
				left+=1
			else:
				right-=1
	
				
	
	return sorted(answers)