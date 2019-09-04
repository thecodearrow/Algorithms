from collections import defaultdict

def minNumberOfJumps(array):
	memo=defaultdict(lambda: float("inf"))
	n=len(array)
	if(n==1):
		return 0
    ans,seenLast=minJumpsRecursive(0,array,n,memo,False)
	if(seenLast):
		return ans
	return -1
	
def minJumpsRecursive(i,array,n,memo,seenLast):
	if(i+array[i]>=n-1):
		seenLast=True
		return 1,seenLast
	if(memo[i] != float("inf")):
		return memo[i],seenLast
	jumps=array[i]
	for j in range(1,jumps+1):
		val,seenLast=minJumpsRecursive(i+j,array,n,memo,seenLast)
		memo[i]=min(memo[i],val)
	memo[i]+=1
	return memo[i],seenLast
	

	