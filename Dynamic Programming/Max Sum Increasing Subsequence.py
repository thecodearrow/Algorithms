#Very similar to LIS

def maxSumIncreasingSubsequence(array):
	n=len(array)
	sum_lis=[ele for ele in array]
	parent=[i for i in range(n)]
	
	for i in range(1,n):
		for j in range(i):
			if(array[j]<array[i]):
				current_sum=array[i]+sum_lis[j]
				if(current_sum>sum_lis[i]):
					sum_lis[i]=current_sum
					parent[i]=j
				
	max_index=0	
	max_sum=-float("inf")
	for i in range(n):
		if(sum_lis[i]>max_sum):
			max_sum=sum_lis[i]
			max_index=i
		
	start=max_index
	ans=[]
	while start!=parent[start]:
		ans.append(array[start])
		start=parent[start]
	ans.append(array[start])
	ans=ans[::-1]
	return [max(sum_lis),ans]
	
