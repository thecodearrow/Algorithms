#https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming


import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp={}
    dp[0]=arr[0]
    if(len(arr)==1):
        return arr[0]
    dp[1]=max(arr[1],arr[0])
    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i],arr[i])
    return dp[len(arr)-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
