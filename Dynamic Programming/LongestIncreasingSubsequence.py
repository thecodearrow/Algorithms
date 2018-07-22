#https://leetcode.com/problems/longest-increasing-subsequence/description/

#O(NLogN) using DP, but you can do better in O(NLogN)


array=[10,9,2,5,3,7,101,18]
n=len(array)
count=[1]*(n) #min value of LIS is 1 

for i in range(1,n):
	current=array[i]
	for j in range(i):
		if(current>array[j]): 
			count[i]=max(count[i],count[j]+1)
 

print(max(count))