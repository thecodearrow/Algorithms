


def can(n,s):
    return (s>=0 and s<=9*n)
    

n,s=[int(x) for x in input().split()]

if(n==1 and s==0):
    print("0 0")
else:
    small=""
    sum=s
    for i in range(1,n+1):
        for d in range(0,10): #checking from 0 to 9
            if(i==1 and d==0):
                continue
            if(can(n-i,s-d)):
                small+=str(d)
                s-=d
                break
    large=""
    s=sum #reset
    for i in range(1,n+1):
        for d in range(9,-1,-1): #checking from 9 to 0
            if(i==1 and d==0):
                continue
            if(can(n-i,s-d)):
                large+=str(d)
                s-=d
                break
    if(small=="" or small[0]=="0"):
        print("-1 -1")
    else:
        
        print(small,large)
                    
                    
    