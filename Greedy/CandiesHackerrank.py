#https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#Greedy Solution



import os
# Complete the candies function below.
def candies(n, arr):
    if(n==1):
        return 1
    candies=[1]*(n)
    

    #forward traversal 

    for i in range(1,n):
        if(arr[i]>arr[i-1]):
            candies[i]=candies[i-1]+1
    print(candies) 
    
    #backwrd traversal 
    for i in range(n-2,-1,-1):
        if(arr[i]>arr[i+1]):
            candies[i]=max(candies[i+1]+1,candies[i]) 
    print(candies)
    return sum(candies)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
