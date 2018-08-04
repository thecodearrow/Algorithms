#https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

#Combines Level Order Traversal + Vertical Order Traversal 

def verticalOrder(root):
    queue=[root]
    hd_given_ele={root.data:0} #horizontal distance
    while queue:
        ele=queue.pop(0)
        if(ele.left):
            l=ele.left.data
            queue.append(ele.left)
            hd_given_ele[l]=hd_given_ele[ele.data]-1
        if(ele.right):
            r=ele.right.data
            queue.append(ele.right)
            hd_given_ele[r]=hd_given_ele[ele.data]+1
        
    return hd_given_ele
    
def printTopView(root):
    hd_ge=verticalOrder(root)
    queue=[root]
    added=set()
    while queue:
        ele=queue.pop(0)
        h=hd_ge[ele.data]
        if(h not in added):
            added.add(h)
            print(ele.data,end=" ")
        if(ele.left):
            queue.append(ele.left)
        if(ele.right):
            queue.append(ele.right)