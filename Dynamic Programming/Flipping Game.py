#Using Kadane's Algo! and slight modification :D

n=int(input())

a=[int(x) for x in input().split()]

#Convert a to b where 0 becomes +1 and 1 becomes -1 

b=[]
ones=0 #no. of ones before flipping
for ele in a:
    if(ele==0):
        b.append(1)
    else:
        b.append(-1)
        ones+=1 
        
answer=ones #we need to try to maximize this value after one flipping

#basically maximize sum of b 

current=0
maximum_sum=-10**9
for ele in b:
    current=max(ele,current+ele)
    maximum_sum=max(maximum_sum,current)

answer=ones+maximum_sum
print(answer)



        
"""#brute force!

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
        """