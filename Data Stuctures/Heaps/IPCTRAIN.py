#https://www.codechef.com/JULY17/problems/IPCTRAIN

#Uses Heap Data Structure
import heapq
t=int(input())
from collections import defaultdict 
while(t!=0):
	t-=1
	day=[]
	num_subs=[]
	sadness=[]
	n,d=[int(x) for x in input().split()]
	for i in range(n):
		temp1,temp2,temp3=[int(x) for x in input().split()]
		day.append(temp1-1)
		num_subs.append(temp2)
		sadness.append(temp3)

	day_dict=defaultdict(list) #key contains list of all trainers available on that day  

	for index in range(n):
		arrival=day[index]
		day_dict[arrival].append((-sadness[index],index)) #(we store as negative values for MAX HEAP!)
		

	sad_count=0 
	teachers=[] #max heap according to sadness 
	for i in range(d):
		#day wise allocation
		#remove from heap if number of days of training already satisfied 
		if(day_dict[i]):
			trainers=day_dict[i]	#index of teachers availale for that day		
			for j in trainers:
				heapq.heappush(teachers,j) #new arrivals
		if(teachers): #non empty heap 
			selected=teachers[0][1] #index of teacher with max sadness 
			num_subs[selected]-=1 
			if(num_subs[selected]==0):
				heapq.heappop(teachers) 
		

	index=0
	sad_count=0
	for i in num_subs:
		sad_count+=sadness[index]*i
		index+=1 

	print(sad_count)






