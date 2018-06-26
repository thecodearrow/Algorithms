#BruteForce O(n^3)

s1="geeksforgeeks"
s2="iamforgeeks"

l1=len(s1)
l2=len(s2)



common=""
maximum=-10**7

for i in range(0,l1):
	for j in range(0,l2):
		idash=i 
		jdash=j
		current_max=0 
		while(idash<l1 and jdash<l2):
			if(s1[idash]!=s2[jdash]):
				break
			if(s1[idash]==s2[jdash]):
				idash+=1
				jdash+=1
				current_max+=1 

			if(maximum<current_max):
					common=s1[i:idash]
					maximum=current_max
	


print(maximum)	
print(common)



