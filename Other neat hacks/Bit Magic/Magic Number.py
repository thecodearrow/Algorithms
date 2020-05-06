"""
Given an integer A, find and return the A'th magic number. 
A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5. 
First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….  
"""
class Solution:
    def solve(self, n):
        answer=0
        fives=1
        while n>0:
            fives*=5
            if(n & 1):
                answer+=fives
            n=n//2
        return answer
        
        
        
        
