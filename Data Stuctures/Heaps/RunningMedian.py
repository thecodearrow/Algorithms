#https://www.hackerrank.com/challenges/find-the-running-median/problem 


import heapq 

#lower half = MAX HEAP
#upper half = MIN HEAP
count={}
count["l_size"]=0
count["u_size"]=0

def addElement(ele,l,u):
	if(count["l_size"]==0 or ele<=(-l[0])):
		heapq.heappush(l,-ele)
		count["l_size"]+=1
	else:
		heapq.heappush(u,ele)
		count["u_size"]+=1
def rebalance(l,u):
	diff=abs(count["l_size"]-count["u_size"])
	if(diff==2):
		if(count["l_size"]>count["u_size"]):
			#transfer from lower to upper 
			ele=-1*heapq.heappop(l)
			heapq.heappush(u,ele)
			#update sizes
			count["l_size"]-=1
			count["u_size"]+=1
		elif(count["l_size"]<count["u_size"]):
			#transfer from upper to lower 
			ele=heapq.heappop(u)
			heapq.heappush(l,-ele)
			#update sizes
			count["l_size"]+=1
			count["u_size"]-=1

def getMedian(l,u):
	if(count["l_size"]==count["u_size"]):
		ele1=-1*l[0]
		ele2=u[0]
		median=(ele1+ele2)/2
	else:
		if(count["l_size"]>count["u_size"]):
			median=-1*l[0]
		else:
			median=u[0]
	return(round(median,1))




n=int(input())

lower=[]
upper=[]
heapq.heapify(lower)
heapq.heapify(upper)

while(n!=0):
	n-=1
	ele=int(input())
	addElement(ele,lower,upper)
	rebalance(lower,upper)
	print(getMedian(lower,upper))
