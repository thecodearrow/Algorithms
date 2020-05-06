fact={}

fact[0]=1 

for i in range(1,5001):
	fact[i]=fact[i-1]*i

def ncr(n, r):
	if(r>n):
		return 0
	return fact[n] // fact[n-r] // fact[r]



#Here's NCR%M

"""
Given three integers A, B and C, where A represents n, B represents r and C represents m, 
find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m. x! means factorial of x i.e. x! = 1 * 2 * 3... * x.   
 
 
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def ncr(self,n,r,m):
        r=min(r,n-r) #ncr = ncn-r
        dp=[0 for j in range(r+1)]
        dp[0]=1
        #Note: This can be solved in O(r) space as only the previous row is required for the computation of the current row
        for i in range(1,n+1):
            #Fill it in reverse since previous two values are needed and it will be replaced if we fill it forward
            for j in range(min(i//2,r),0,-1):
                dp[j]=(dp[j]+dp[j-1])%m
            #ncr = ncn-r
            for j in range(i//2+1,r+1):
                dp[j]=dp[i-j]
        return dp[r]
            
        
        
    def solve(self, n, r, m):
        return self.ncr(n,r,m)