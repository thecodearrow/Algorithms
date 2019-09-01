#https://www.spoj.com/problems/MSTICK/
import functools
import bisect
import math
def cmp(a,b):
    l1,w1=a[0],a[1]
    l2,w2=b[0],b[1]
    if(l1==l2):
        if(w1<w2):
            return -1
        else:
            return 1
    else:
        if(l1<l2):
            return -1
        else:
            return 1
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    temp=[int(x) for x in input().split()]
    sticks=[]
    for i in range(0,2*n,2):
        sticks.append([temp[i],temp[i+1]])
    sticks=sorted(sticks,key=functools.cmp_to_key(cmp))
    available_sticks=[sticks[0]]
    sticks_by_weight=[sticks[0][1]]
    count=1
    for i in range(1,n):
        low=0
        high=count
        l,w=sticks[i]
        while low<high:
            mid=(low+high)//2
            lmid,wmid=available_sticks[mid]
            if(w>=wmid):
                high=mid
            else:
                low=mid+1
        pos=high
        if(pos<count):
            available_sticks[pos][1]=w
            sticks_by_weight[pos]=w
        else:
            count+=1
            available_sticks.append([l,w])
            sticks_by_weight.append(w)
            
        #print(pos,available_sticks)
    print(count)





