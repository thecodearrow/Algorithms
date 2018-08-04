#https://leetcode.com/problems/sliding-window-maximum/description/

nums = [1,3,-1,-3,5,3,6,7]
n=len(nums)
k=3
currentWindowSum=0

for i in range(k):
	currentWindowSum+=nums[i]

maxWindowSum=currentWindowSum
for i in range(n-k):
	currentWindowSum-=nums[i]
	currentWindowSum+=nums[i+k]
	maxWindowSum=max(maxWindowSum,currentWindowSum)

print(maxWindowSum)