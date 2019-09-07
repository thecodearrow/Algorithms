def knapsackProblem(items, capacity):
    # Write your code here.
	items=[[]]+items
	n=len(items)
	if(n==0 or capacity==0):
		return [0,[]]
	memo=[[0 for i in range(capacity+1)]for j in range(n)]
	for i in range(1,n):
		val,weight=items[i][0],items[i][1]
		for j in range(capacity+1):
			if(weight<=j):
				memo[i][j]=max(memo[i-1][j-weight]+val,memo[i-1][j])
			else:
				memo[i][j]=memo[i-1][j]
	
	i=n-1
	j=capacity
	knapsack=[]
	#printing the items chosen
	while(j!=0 and i>0):
		val,weight=items[i][0],items[i][1]
		if(memo[i][j]!=memo[i-1][j]):
			knapsack.append(i-1)
			j=j-weight
		i=i-1
			
	return [memo[n-1][capacity],knapsack[::-1]]
				
			