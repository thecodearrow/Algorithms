#include <bits/stdc++.h>
using namespace std;
// To heapify a subtree rooted with node i which is
// an index in arr[]. n is size of heap
void heapify(int arr[], int n, int i);
void buildHeap(int arr[], int n);
// main function to do heap sort
void heapSort(int arr[], int n)
{
    buildHeap(arr, n);
    for (int i=n-1; i>=0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("
");
}
// Driver program to test above functions
int main()
{
    int arr[1000000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
    heapSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}


/*This is a function problem.You only need to complete the function given below*/
/* Main function to do heap sort. This function uses buildHeap()
   and heapify()
void heapSort(int arr[], int n)  {
    buildHeap(arr, n);
    for (int i=n-1; i>=0; i--)  {
        swap(arr[0], arr[i]);
        int heapsize=i; //reducing it by 1 each time
        heapify(arr, heapsize, 0);
    }
} */
// The functions should be written in a way that array become sorted 
// in increasing order when above heapSort() is called.
// To heapify a subtree rooted with node i which is  an index in arr[]. 
// n is size of heap. This function  is used in above heapSort()
void heapify(int arr[], int n, int i)  {
      // Your Code Here
      int l=2*i+1;
      int r=2*i+2;
      int largestNodeIndex=i;
      if(l<n && arr[l]>arr[largestNodeIndex]){
          largestNodeIndex=l;
      }
      if(r<n && arr[r]>arr[largestNodeIndex]){
          largestNodeIndex=r;
      }
      if(largestNodeIndex!=i){
          swap(arr[i],arr[largestNodeIndex]);
          heapify(arr,n,largestNodeIndex);
      }
}
// Rearranges input array so that it becomes a max heap
void buildHeap(int arr[], int n)  { 
    // Start from a non leaf node and go till node 0
    //Max Heapify it at that node
    int nonLeafIndex=(n/2)-1;
    for(int i=nonLeafIndex;i>=0;i--){
        heapify(arr,n,i);
    }
    
}