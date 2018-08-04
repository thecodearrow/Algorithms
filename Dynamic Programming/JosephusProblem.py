#https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle/0

#WINNER[N,K]=( WINNER[N-1,K] + K ) %  N 

t=int(input())

while t!=0:
	t-=1
	n,k=[int(x) for x in input().split()]
	winner={}

	winner[1]=0

	for i in range(2,n+1):
		winner[i]=(winner[i-1]+k)%i 

	print(winner[n]+1)

