#Find quadruplets in array that add up to the targetSum

def fourNumberSum(a, targetSum):
	answers=[]
	n=len(a)
	a=sorted(a)
	for i in range(n-3):
		w=a[i]
		for j in range(i+1,n-2):
			x=a[j]
			left=j+1
			right=n-1
			while left<right:
				y=a[left]
				z=a[right]
				if(w+x+y+z==targetSum):
					answers.append(sorted([w,x,y,z]))
				if(w+x+y+z<targetSum):
					left+=1
				else:
					right-=1
				
	return sorted(answers)