#https://codeforces.com/contest/991 
#Binary Search


n=int(input())

def petya(n, k):
    total = n
    s = 0

    while n > 0:
        cur = min(n, k)
        s += cur
        n -= cur

        n -= n // 10

    return s * 2 >= total


low=1
high=n
candies=n
aim=candies/2 
mid=1
ans=1


while low<=high:
	mid=(low+high)//2 
	if(petya(candies,mid)):
		ans=mid
		high=mid-1

	else:
		low=mid+1

	


print(ans)





