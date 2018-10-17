#https://www.interviewbit.com/problems/maximum-consecutive-gap/

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

"""

# gap = (MAX - MIN) / (N - 1)

#Our answer will lie between [gap,MAX-MIN]
import math
from collections import defaultdict
class Solution:
    
    def maximumGap(self, A):
      
        if(len(A)==1):
            return 0
        if(len(A)==2):
            return A[1]-A[0]
        MAX=max(A)+1
        MIN=min(A)-1
        n=len(A)
        gap=(MAX-MIN)/(n-1)
        gap=math.ceil(gap)
        bucket=defaultdict(list)
        if((MAX-1)-(MIN+1)==0):
            return 0 #contains the same numbers

        #BUCKETING STEP
        for ele in A:
            g=int((ele-MIN)/gap)
            idx=g
            bucket[idx].append(ele)

        bucket_list=sorted(list(bucket))
        
        maximum=0
        diff=A[2]-A[1]
        
        #CALCULATION STEP
        
        for i in range(len(bucket_list)-1):
            b1=bucket_list[i]
            b2=bucket_list[i+1]
            item1=max(bucket[b1])
            item2=min(bucket[b2])
            diff=int(item2-item1)
            maximum=max(diff,maximum)


        return maximum


      