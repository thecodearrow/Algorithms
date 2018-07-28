import math
def checkCorrectK(bananas,k,h):
    count=0
    for b in bananas:
        count+=math.ceil(b/k) 
    if(count<=h):
        return True
    else:
        return False
        


def binarySearch(bananas,h):
    low=1 
    high=max(bananas)
    ans=0
    while(low<=high):
        mid=(low+high)//2
        if(checkCorrectK(bananas,mid,h)):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    
 
t=int(input())
while(t!=0):
    t=t-1
    n,h=[int(x) for x in input().strip().split()]
    bananas=[int(x) for x in input().strip().split()]
    print(binarySearch(bananas,h))