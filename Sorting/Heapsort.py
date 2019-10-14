def maxHeapify(a,pos,n):
    left_i=2*pos+1
    right_i=2*pos+2
    largestNodeIndex=pos
    if(left_i<n and a[left_i]>a[largestNodeIndex]):
        largestNodeIndex=left_i
    if(right_i<n and a[right_i]>a[largestNodeIndex]):
        largestNodeIndex=right_i

    #Bubble down 
    if(largestNodeIndex!=pos):
        a[largestNodeIndex],a[pos]=a[pos],a[largestNodeIndex]
        maxHeapify(a,largestNodeIndex,n)

def buildMaxHeap(a):
    n=len(a)
    nonLeafNodeIndex=(n//2)-1
    for i in range(nonLeafNodeIndex,-1,-1):
        maxHeapify(a,i,n)

    
def heapSort(a):
    n=len(a)
    buildMaxHeap(a)
    heapSize=n
    for i in range(n-1,-1,-1):
        a[0],a[i]=a[i],a[0] #Swapping the largest element to the end of array
        heapSize-=1
        maxHeapify(a,0,heapSize)

    

arr=[8,4,1,5,6,7,2,3]
heapSort(arr)
print(arr)


