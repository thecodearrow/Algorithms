#https://www.spoj.com/problems/MDOLLS/
import sys
import functools
import bisect
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

"""
O(n^2 solution DP)
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    dolls=[]
    for i in range(0,2*n,2):
        dolls.append([a[i],a[i+1]])

    dolls=sorted(dolls)
    possible_answers=[1 for i in range(n)] #LIS
    for i in range(1,n):
        w1,h1=dolls[i]
        for j in range(i):
            w2,h2=dolls[j]
            if(w1<w2 and h1<h2):
                possible_answers[i]=max(possible_answers[i],possible_answers[j]+1)
    possible_answers=[n+1-i for i in range(n)] 
    print(min(possible_answers))

"""

t=int(input())
def cmp(a,b):
    w1,h1=a[0],a[1]
    w2,h2=b[0],b[1]
    if(w1==w2):
        if(h1<h2):
            return -1
        else:
            return 1
    else:
        if(w1>w2):
            return -1
        else:
            return 1
      
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    dolls=[]
    for i in range(0,2*n,2):
        dolls.append([a[i],a[i+1]])

    dolls=sorted(dolls,key=functools.cmp_to_key(cmp))
    available_dolls=[dolls[0]]
    dolls_heightwise=[dolls[0][1]]
    count=1
    for i in range(1,n):
        w,h=dolls[i]
        #pos=bisect.bisect_right(dolls_heightwise,h)
        pos=0
        if(pos<count):
            #possible to nest doll
            available_dolls[pos]=[w,h]
            dolls_heightwise[pos]=h
        else:
            #not possible to nest, so add doll to available dolls
            available_dolls.append([w,h])
            dolls_heightwise.append(h)
            count+=1
    print(count)
    
