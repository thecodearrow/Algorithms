
def hash(string):
	prime=101
	h=0
	i=0
	for s in string:
		h+=ord(s)*pow(prime,i)
		i+=1

	return h

def isSubstring(s1,s2):
	window=len(s2)
	substring_hash=hash(s2)
	substring=""
	for i in range(len(s1)-window+1):
		substring=""
		for j in range(window):
			substring+=s1[i+j]
		print(substring)
		if(hash(substring)==substring_hash):
			return i



	return False



string="Harry"
substring="ry"
print(isSubstring(string,substring))