#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

#Very Interesting two ponter

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls=len(s)
        lp=len(p)
        chars_count=Counter(p)
        i,j=0,0
        ans=[]
        while j<ls:
            if(chars_count[s[j]]>0):
                chars_count[s[j]]-=1
                j+=1
                if(j-i==lp):
                    ans.append(i)
            elif(i==j):
                i+=1
                j+=1
            elif(chars_count[s[j]]<=0):
                chars_count[s[i]]+=1
                i+=1
            
            
            
                
        return ans
        
