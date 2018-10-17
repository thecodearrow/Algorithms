#http://codeforces.com/contest/1065/problem/C

import sys

try:
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
except:
	pass
	

n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]

chop=min(a)
a=[x-chop for x in a]
slices=0
h_greater={}
a=sorted(a)[::-1]
pos=1
for h in a:
	h_greater[h]=pos
	pos+=1 


heights=[]
prev=h_greater[max(a)]
for i in range(max(a),0,-1):
	if(i in h_greater):
		heights.append(h_greater[i])
		prev=h_greater[i]

	else:
		heights.append(prev)



slices=1
count=0
for h in heights:
	if(count+h>k):
		count=0
		slices+=1
	count+=h 
	

flag=True #check if every element if already equal

for ele in a:
	if(ele!=0):
		flag=False 
		break 

if(not flag):
	print(slices)
else:
	print(0)