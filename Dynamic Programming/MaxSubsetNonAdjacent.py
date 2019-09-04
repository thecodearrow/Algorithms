"""
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent 
in the array. 
So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.
"""


def maxSubsetSumNoAdjacent(array):
	n=len(array)
	if(n==0):
		return 0
	if(n==1):
		return array[0]
	best_without=array[0]
	best_with=max(array[0],array[1])
	current_best=max(best_without,best_with)
	for i in range(2,n):
		ele=array[i]
		current_best=max(best_without+ele,best_with)
		best_without=best_with
		best_with=current_best
	return current_best
	
	
	