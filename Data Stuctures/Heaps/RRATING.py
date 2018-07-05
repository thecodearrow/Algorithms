#https://www.codechef.com/problems/RRATING
import heapq
n=int(input())
size=0

#I'll maintain 2 heaps-- HEAP1 (MIN HEAP) for the first one third elements (descending order) 
#HEAP2 (MAX HEAP) for remaining elements 

count={"h1":0,"h2":0,"size":0}

heap1=[]
heap2=[]
heapq.heapify(heap1)
heapq.heapify(heap2)
def addElement(e,h1,h2):
	if(count["h1"]!=0 and e>h1[0]):
		heapq.heappush(h1,e)
		count["h1"]+=1
	else:
		heapq.heappush(h2,-e)
		count["h2"]+=1

def rebalance(h1,h2):
	floorval=count["size"]//3
	if(count["h1"]>floorval):
		ele=heapq.heappop(heap1)
		heapq.heappush(heap2,-ele)
		count["h2"]+=1
		count["h1"]-=1
	elif(count["h1"]<floorval):
		ele=heapq.heappop(heap2)
		heapq.heappush(heap1,-ele)
		count["h1"]+=1
		count["h2"]-=1


while(n!=0):
	n-=1
	temp=[int(x) for x in input().split()]
	if(temp[0]==1):
		ele=temp[1]
		size+=1
		count["size"]+=1
		addElement(ele,heap1,heap2)
		rebalance(heap1,heap2)
		
	else:
		#print from heap1

		one_third=size//3
		if(one_third!=0):
			print(heap1[0])
		else:
			print("No reviews yet")