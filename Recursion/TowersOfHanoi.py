#Ultimate Recursion Problem

count={"cnt":0}
def toh(n,source,aux,dest):
	if(n==0):
		return 
	count["cnt"]+=1 
	toh(n-1,source,dest,aux)
	print("Moving disk",n,"from",source,"to",dest)
	toh(n-1,aux,source,dest)


toh(5,"A","B","C")
print("Brahma says this can be achieved in",count["cnt"],"moves! ;)")