#https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
#https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

import bisect
def longestIncreasingSubsequence(array):
    n=len(array)
	parent=[-1 for i in range(n)]
	sequence=[[array[0],0]] #(ele,pos)
	l=1
	for i in range(1,n):
		ele=array[i]
		if(ele>sequence[-1][0]):
			parent[i]=sequence[-1][1]
			sequence.append([ele,i])
			l+=1
		else:
			#Use Binary Search to find pos
			pos=bisect.bisect_left(sequence,[ele,i])
			sequence[pos]=[ele,i]
			if(pos>0):
				parent[i]=sequence[pos-1][1]
				
	ans=[]
	start_index=sequence[-1][1]
	while(start_index!=-1):
		ans.append(array[start_index])
		start_index=parent[start_index]
	
	return ans[::-1]
	