def storePowersets(index,n,array,current_set,power_sets):
	if(index==n):
		return
	storePowersets(index+1,n,array,current_set,power_sets)
	current_element=array[index]
	newSet=current_set.append(current_element)
	power_sets.append(newSet)
	storePowersets(index+1,n,array,newSet,power_sets)
	
def powerset(array):
	n=len(array)
	power_sets=[[]]
	storePowersets(0,n,array,[],power_sets)
	return power_sets



	
#Iterative solution

def storePowersetsIterative(array):
	power_sets=[[]]
	for ele in array:
		current_powersets_length=len(power_sets)
		for i in range(current_powersets_length):
			current_power_set=power_sets[i]
			power_sets.append(current_power_set+[ele])
	return power_sets