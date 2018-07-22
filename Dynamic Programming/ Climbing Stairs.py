#https://leetcode.com/problems/climbing-stairs/description/

n=int(input())
f={} 
f[0]=1
f[1]=1 
for i in range(2,n+1):
	f[i]=f[i-1]+f[i-2]

print(f[n])