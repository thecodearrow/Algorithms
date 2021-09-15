  #Z-Algorithm for substring matching
  
  def getZArr(s):
        n=len(s)
        z=[0]*n
        z[0]=n
        l,r=0,0
        for i in range(1,n):
            if(i>r):
                #brute force (we haven't computed it yet)
                l,r=i,i
                while r<n and s[r]==s[r-l]:
                    r+=1
                z[i]=r-l
                r-=1 #mismatch (shot by 1)
            else:
                if(i+z[i-l]<=r):
                    #no need to recompute!
                    z[i]=z[i-l]
                else:
                    l=i
                    while r<n and s[r]==s[r-l]:
                        r+=1
                    z[i]=r-l
                    r-=1 #mismatch (shot by 1)
        
        return z
      
      
     #to find pattern m in string n
    
    s=m+"#"+n #pattern as a prefix! 
    z=getZArr(s)
