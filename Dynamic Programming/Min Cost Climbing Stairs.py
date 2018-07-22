#https://leetcode.com/problems/min-cost-climbing-stairs/description/

steps=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1,0] #adding 0 since I need to get outside the array!

f={}
f[0]=steps[0]
f[1]=steps[1]
for i in range(2,len(steps)):
	f[i]=steps[i]+min(f[i-1],f[i-2])

print(f[len(steps)-1])