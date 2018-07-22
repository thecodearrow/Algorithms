#https://leetcode.com/problems/edit-distance/description/

#Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

word1 = "0horse"  #source
word2 = "0ros"    #destination

dp=[]
for i in range(len(word1)+1):
	dp.append([])
	for j in range(len(word2)+1):
		dp[i].append(0)

#initializations in the null strings row wise and col wise

for i in range(len(word1)+1):
	dp[i][0]=i

for i in range(len(word2)+1):
	dp[0][i]=i

for i in range(1,len(word1)+1):
	w1=word1[i]
	for j in range(1,len(word2)+1):
		w2=word2[j]
		if(w1==w2):
			dp[i][j]=dp[i-1][j-1] #no operation 
		else:
			dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 #best of delete,add,replace +1 

print(dp[len(word1)][len(word2)])