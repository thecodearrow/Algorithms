

def findClosestBST(node,target,closest):
	if(node==None):
		return closest
	difference=abs(node.value-target)
	if(difference<abs(closest-target)):
		closest=node.value
	if(target==node.value):
		closest=node.value
		return node.value
	elif(node.value<target):
		return findClosestBST(node.right,target,closest)
	else:
		return findClosestBST(node.left,target,closest)
		
def findClosestValueInBst(tree, target):
    # Write your code here.
	closestValue=findClosestBST(tree,target,float("inf"))
	return closestValue
	
		
	
