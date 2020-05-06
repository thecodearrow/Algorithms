#Reference
#https://www.youtube.com/watch?v=M5FWpJTqC40

#https://www.codechef.com/problems/SHUFFLE

from collections import defaultdict
import math
t=int(input())
while t!=0:
    t-=1 
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    split_lists=defaultdict(list)
    for i in range(n):
        mod_i=i%k 
        split_lists[mod_i].append(a[i])
    
    new_list=[]
    #sort each list
    for i in range(k):
        split_lists[i]=sorted(split_lists[i])
        
    #Merge together!
    limit=math.ceil(n/k)
    for i in range(limit):
        for j in range(k):
            if(i<len(split_lists[j])):
                new_list.append(split_lists[j][i])
    
    can_sort=True
    #print(new_list)
    #If new_list is not sorted, original list cannot be sorted
    
    for i in range(1,len(new_list)):
        if(new_list[i-1]>new_list[i]):
            can_sort=False
            break
    if(can_sort):
        print("yes")
    else:
        print("no")