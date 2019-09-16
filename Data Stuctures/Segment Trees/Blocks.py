#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/blocks-2/description/


import sys
import math
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


class SegmentTree():
    def __init__(self):
        self.seg_tree=defaultdict(lambda:0)
        self.lazy=defaultdict(lambda:0)

    def lazy_prop(self,key,low,high):
        mid=(low+high)//2
        left_key=2*key+1
        right_key=2*key+2
        self.lazy[left_key]=self.lazy[key]
        self.lazy[right_key]=self.lazy[key]
        self.seg_tree[key]=self.lazy[key]
        self.lazy[key]=0 

    def query(self,key,low,high,qlow,qhigh):
        if(self.lazy[key]!=0):
            self.lazy_prop(key,low,high)
        if(low>high or high<qlow or low>qhigh):
            #no overlap
            return 0
        if(low>=qlow and high<=qhigh):
            #total overlap
            return self.seg_tree[key]
        #partial overlap
        mid=(low+high)//2
        left_key=2*key+1
        right_key=2*key+2
        return max(self.query(left_key,low,mid,qlow,qhigh),self.query(right_key,mid+1,high,qlow,qhigh))




    def update(self,key,low,high,qlow,qhigh,height):
        mid=(low+high)//2
        if(self.lazy[key]!=0):
            self.lazy_prop(key,low,high)
        if(low>high or high<qlow or low>qhigh):
            #no overlap
            return 0
        
        if(low>=qlow and high<=qhigh):
            #total overlap
            left_key=2*key+1
            right_key=2*key+2
            self.seg_tree[key]=height
            self.lazy[left_key]=height
            self.lazy[right_key]=height
            return self.seg_tree[key]
        left_key=2*key+1
        right_key=2*key+2
        self.seg_tree[key]=max(self.update(left_key,low,mid,qlow,qhigh,height),self.update(right_key,mid+1,high,qlow,qhigh,height))
        return self.seg_tree[key]
        





n=int(input())
blocks=[]
ranges=[]
for i in range(n):
    l,h,p,c,x=[int(x) for x in input().split()]
    blocks.append([l,h,p,c,x])
    ranges.append(x)
    ranges.append(x+l-1)

ranges=sorted(ranges)
start=ranges[0]
end=ranges[-1]
s=SegmentTree()
for l,h,p,c,x in blocks:
    current_max_height=s.query(0,start,end,x,x+l-1)
    if(c==1):
        s.update(0,start,end,x,x+l-1,current_max_height+1)
        s.update(0,start,end,x+p-1,x+p-1,h+current_max_height+1)
    else:
        height_at_p=s.query(0,start,end,x+p-1,x+p-1)
        if((h+height_at_p)>current_max_height):
            s.update(0,start,end,x,x+l-1,height_at_p+h+1)
        else:
            s.update(0,start,end,x,x+l-1,current_max_height+1)
            

print(s.seg_tree[0])







    