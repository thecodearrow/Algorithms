#https://www.codechef.com/ALMOCK01/problems/CHEFD
"""

Chef has an array containing N integers. You have to make M queries. Each query has one of the two types:

1 l r p - Select all the numbers having indices between l and r (inclusive) that are divisible by p and divide them by p, where p is in set {2, 3, 5}.
2 l d - Modify the l-th number in the array to d.
Please help Chef in finding out the array after all the M queries.


"""
n=int(input())
a=[int(x) for x in input().split()]
q=int(input())
for query in range(q):
	temp=[int(x) for x in input().split()]
	if(temp[0]==1):
		L=temp[1]-1
		R=temp[2]-1
		p=temp[3]
		for i in range(L,R+1):
			if(a[i]%p==0):
				a[i]/=p
	else:
		index=temp[1]-1
		ele=temp[2]
		a[index]=ele 


for i in a:
	print(int(i),end=' ')