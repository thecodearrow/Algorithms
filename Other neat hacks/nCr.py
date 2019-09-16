fact={}

fact[0]=1 

for i in range(1,5001):
	fact[i]=fact[i-1]*i

def ncr(n, r):
	if(r>n):
		return 0
	return fact[n] // fact[n-r] // fact[r]