#Mahesh and his lost array 
#https://www.codechef.com/problems/ANUMLA 
 
#TLE :(
import heapq 
t=int(input())
 
while(t!=0):
	t-=1 
	n=int(input())
	paper_values=[int(x) for x in input().split()]
	heapq.heapify(paper_values)  
	heapq.heappop(paper_values) #0
	a1=heapq.heappop(paper_values) #a1
	a=[a1]
	combos=[a1]
	while(paper_values):
		ele=heapq.heappop(paper_values) #smallest 
		a.append(ele)
		to_be_added=[]
		for x in combos:
			paper_values.remove(x+ele)  #THIS IS BAD
			to_be_added.append(x+ele)
 
		for x in to_be_added:
			combos.append(x)
		combos.append(ele)
 
		#reheapify
		heapq.heapify(paper_values)
 
 
 
	for ele in a:
		print(ele,end=' ')
	print() 