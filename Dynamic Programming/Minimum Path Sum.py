#https://leetcode.com/problems/minimum-path-sum/description/

grid=[[1,3,1],[1,5,1],[4,2,1]]
dp={}
n=len(grid)
m=len(grid[0])

#updating first row
dp[0,0]=grid[0][0]
for i in range(1,m):
	dp[0,i]=grid[0][i]+dp[0,i-1]

for i in range(1,n):
	dp[i,0]=grid[i][0]+dp[i-1,0]

for i in range(1,n):
	for j in range(1,m):
		dp[i,j]=grid[i][j]+min(dp[i,j-1],dp[i-1,j])

print(dp[n-1,m-1])