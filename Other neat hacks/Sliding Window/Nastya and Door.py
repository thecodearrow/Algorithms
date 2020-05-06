#https://codeforces.com/contest/1341/problem/B


import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    input = sys.stdin.readline 
    

def takeInput():
    return [int(x) for x in input().strip().split()]
 
        
t=int(input())
while t!=0:
    t-=1
    n,k=takeInput()
    a=takeInput()
    peaks=[0 for i in range(n)]
    for i in range(1,n-1):
        if(a[i-1]<a[i] and a[i]>a[i+1]):
            peaks[i]=1

    p=0
    window_size=k-2
    peaks_found=0
    for i in range(1,window_size+1):
        if(peaks[i]):
            peaks_found+=1
    current_ans=peaks_found
    start=0
    for i in range(window_size+1,n):
        peaks_found-=peaks[i-window_size]
        peaks_found+=peaks[i]
        if(peaks_found>current_ans):
            #print(a[i-window_size+1:i+1])
            current_ans=peaks_found
            start=i-window_size
        

    print(current_ans+1,start+1)
        


    






