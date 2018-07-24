#https://leetcode.com/problems/house-robber/description/

houses=[2,7,9,3,1]
l=len(houses)

if(l==1):
	print(houses[0])
elif(l==0):
	print(0)
else:
#Let us try solving for only two houses

	best={}
	best[0]=houses[0]
	best[1]=max(houses[0],houses[1])

	for i in range(2,l):
		best[i]=max(houses[i]+best[i-2],best[i-1]) #i choose to rob this house or i don't rob this house! 

	print(best[l-1])