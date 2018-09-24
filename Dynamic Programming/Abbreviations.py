#https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

from collections import defaultdict
t=int(input())

while t!=0:
    t-=1
    a=input()
    b=input()

    dp=defaultdict(lambda:False,{})
    dp[0,0]=True
    a=['']+list(a)
    b=['']+list(b)
    l1=len(a)
    l2=len(b)

    
    #null level

    for i in range(1,l1):
        c=a[i]
        if(c.islower() and dp[0,i-1]):
            dp[0,i]=True


    for i in range(1,l2):
        c1=b[i]
        for j in range(1,l1):
            c2=a[j]
            if(c2.upper()==c1):
                #match 
                if(dp[i-1,j-1] or dp[i,j-1]):
                    dp[i,j]=True
            elif(c2.islower() and dp[i,j-1]):
                #lower case
                dp[i,j]=True

  
    if(dp[l2-1,l1-1]):
        print("YES")
    else:
        print("NO")



