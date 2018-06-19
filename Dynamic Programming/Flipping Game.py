#brute force!

n=int(input())

a=[int(x) for x in input().split()]

maximum=-10**7 #-inf
current=0
ones_from_front=0 



for i in range(0,n):
    for j in range(i,n):
        array=list(a)
        current=0
        for k in range(0,n):
            if(i<=k and k<=j):
                array[k]=1-array[k]
                
            if(array[k]==1):
                current+=1
    
        maximum=max(maximum,current)
            
    
            

print(maximum)
        