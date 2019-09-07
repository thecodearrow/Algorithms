"""
Given disks of width,depth and height, find the pile of disks with greatest height
 that can be stacked up such that the w,d,h of the disk above is strictly less than the one below.
"""

def diskStacking(disks):
    #sort by increasing order of heights
    disks=sorted(disks,key=lambda x:x[2])
    n=len(disks)
    max_heights=[h for w,d,h in disks]
    parent=[None for i in range(n)]
    current_max_height=max_heights[0]
    current_max_height_index=0
    for i in range(1,n):
        w1,d1,h1=disks[i][0],disks[i][1],disks[i][2]
        height_max_info=[0,None] #storing the max disk of smaller height than i that can be piled up
            w2,d2,h2=disks[j][0],disks[j][1],disks[j][2]
            if(w2<w1 and d2<d1 and h2<h1):
                current_height=max_heights[j]
                if(current_height>height_max_info[0]):
                    height_max_info=[max_heights[j],j]
        h,index=height_max_info
        max_heights[i]+=h
        parent[i]=index
        #Storing the pile with greatest total height to backtrack later
        if(current_max_height<max_heights[i]):
            current_max_height=max_heights[i]
            current_max_height_index=i
    #Backtracking to find the pile
    start=current_max_height_index
    stack=[]
    while(start!=None):
        stack.append(disks[start])
        start=parent[start]
            
            
    return stack[::-1]
