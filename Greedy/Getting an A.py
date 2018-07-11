#https://codeforces.com/contest/991
#greedy approach

n=int(input())

a=[int(x) for x in input().split()]
a=sorted(a)
greedy=0
s=sum(a)
done=False
avg=s/n
if(avg>=4.5):
	done=True
for m in a:
	if(done):
		break
	if(m!=5):	
		greedy+=1
	to_be_added=5-m
	s+=to_be_added
	avg=s/n 
	if(avg>=4.5):
		
	
		break 

print(greedy)
