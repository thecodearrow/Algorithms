"""
Given a list of numbers and N digits of pi, find the minimum no. of spaces to be added in the pi string such
 that resultant subtrings are present in the given list of numbers
"""

def numbersInPi(pi, numbers):
    # Write your code here.
	spaces=0
	favourites=set()
	for n in numbers:
		favourites.add(n)
	n=len(pi)
	ans=minSpaces("",pi,favourites,n,{})
	if(ans==float("inf")):
		return -1
	return ans

def minSpaces(prefix,suffix,favourites,n,memo):
	key=prefix+":"+suffix
	if(suffix==""):
		if(prefix in favourites):
			return 0
		return float("inf")
	if(key in memo):
		return memo[key]	
	prefix+=suffix[0]
	if(prefix in favourites):
		memo[key]=min(minSpaces(prefix,suffix[1:],favourites,n,memo),1+minSpaces("",suffix[1:],favourites,n,memo))
	else:
		memo[key]=minSpaces(prefix,suffix[1:],favourites,n,memo)
	return memo[key]
	
	
	
	
			