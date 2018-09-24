#An algorithm that ensures uniform shuffling (every permutation is equally likely)
import random
def KFY(arr):
	n=len(arr)
	for i in range(n):
		idx1=i 
		idx2=random.randrange(i,n) 

		#idx2=random.randrange(0,n) #NAIVE SHUFFLE BIG MISTAKE! CodeChef problem!:P 
		arr[idx1],arr[idx2]=arr[idx2],arr[idx1]

	return arr 


print(KFY([1,2,3,4,5,6,7,8,9,10]))
