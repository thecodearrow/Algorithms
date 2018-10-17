
text=['Text','mining','is','a','fun','subject','to','study']
line_width=10
badness=[]
INF=10**9+7
N=len(text)

#Calculating badness[i,j]


for i in range(N):
	badness.append([])
	current=0
	for j in range(N):
		if(j<i):
			badness[i].append(INF)
		else:
			current+=len(text[j])
			val=(line_width-current)
			if(val>=0):
				badness[i].append(val**2)
			else:
				badness[i].append(INF)
			current+=1


dp=[0]*N
split_at=[0]*N

#deciding where to split so as to ensure optimal text justification
#using dynamic programming!

for i in range(N-1,-1,-1):
	min_j=N
	current_min=badness[i][N-1]
	for j in range(N-1,i,-1):
		if(badness[i][j-1]<INF):
			val=badness[i][j-1]+dp[j]
			if(val<current_min):
				min_j=j
				current_min=val
	
	dp[i]=current_min
	split_at[i]=min_j



#PRINTS THE TEXT OF STRINGS IN A JUSFTIFIED MANNER using split_at array

seen=set()
line_break=[]
for i in split_at:
	if(i not in seen):
		line_break.append(i)
	seen.add(i)

current=0
for b in line_break:
	for j in range(current,b):
		print(text[j],end=" ")
	current=b
	print() #newline





