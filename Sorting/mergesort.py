
a=[100,33,66,45,67,67,89,1,2,3]


def mergesort(start,end):
    if(start==end):
        return 0

    mid=(start+end)//2    
    mergesort(start,mid)
    mergesort(mid+1,end)
    merge(start,mid,end)
    if(start==0 and end==len(a)-1):
        return a
    



def merge(start,mid,end):
    i=0
    j=0
    k=start
    L=a[start:mid+1]
    R=a[mid+1:end+1]
    while(i<=(mid-start) and j<=(end-mid-1)):
        if(L[i]<=R[j]):
            a[k]=L[i]
            i+=1
            k+=1
        else:
            a[k]=R[j]
            j+=1
            k+=1
        

    while(i<=mid-start):
        a[k]=L[i]
        i+=1
        k+=1
    while(j<end-mid-1):
        a[k]=R[j]
        j+=1
        k+=1



ans=mergesort(0,9)
print(ans)





