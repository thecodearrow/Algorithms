#Given a string find the mininum no. of cuts to make all the substrings after cut a palindrome. 

def isPalindrome(s):
	if(s==""):
		return False
	return s==s[::-1]
	
def palindromePartitioningMinCuts(string):
    return minCuts("",string,{})

def minCuts(prefix,suffix,memo):
	key=prefix+":"+suffix
	if(suffix==""):
		if(isPalindrome(prefix)):
			return 0
		else:
			return len(prefix)-1
	if(key in memo):
		return memo[key]
	prefix+=suffix[0]
	if(isPalindrome(prefix)):
		minCuts1=1+minCuts("",suffix[1:],memo)
		minCuts2=minCuts(prefix,suffix[1:],memo)
		memo[key]=min(minCuts1,minCuts2)
	else:
		memo[key]=minCuts(prefix,suffix[1:],memo)
	return memo[key]
		
	
