#Check if s1 is a subsequence of s2 

def isSubSeq(s1,s2):
    #considering s1 is shorter 
    l1=len(s1)
    l2=len(s2)
    if(l1>l2):
        s1,s2=s2,s1 
        l1,l2=l2,l1
    
    j=0
    for i in range(l2):
        if(j<l1):
            if(s2[i]==s1[j]):
                j+=1 
    
    if(j==l1):
        #s2 contains all characters in s1
        return True 
    return False
