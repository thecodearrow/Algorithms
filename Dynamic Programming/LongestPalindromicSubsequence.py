#https://leetcode.com/problems/longest-palindromic-subsequence/description/ 

#TLE 
#65 / 83 test cases passed.

#It's the same as Longest Common Subsequence DP problem where here s2= reverse(s1)

from collections import defaultdict
class Solution:
    def longestPalindromeSubseq(self, s):
        s1=s
        s2=s[::-1]
        maxLen=0
        dp=defaultdict(lambda:0)
        l=len(s)
        for i in range(l):
            for j in range(l):
                if(s1[i]==s2[j]):
                    dp[(i,j)]=1+dp[(i-1,j-1)]
                else:
                    dp[(i,j)]=max(+dp[(i-1,j)],+dp[(i,j-1)])
                if(dp[(i,j)]>maxLen):    
                    maxLen=dp[(i,j)]
                    
     
        return maxLen
                
        