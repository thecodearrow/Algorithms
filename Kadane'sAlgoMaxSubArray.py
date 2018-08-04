a=[-6, -7, -9, 2, 4, 3, 1, -8, -6, -7]


#Kadane's Algo!

def maxSubArrayKadane(a):
    answer_max=current_max=a[0]
    
    for i in range(1,len(a)):
        current_max=max(a[i],current_max+a[i]) 
        """
        if(current_max>0):
        	current_max+=a[i]
        else:
        	current_max=a[i]
        """
        if(current_max>answer_max):
            answer_max=current_max
    return(answer_max)
    
    
print(maxSubArrayKadane(a))