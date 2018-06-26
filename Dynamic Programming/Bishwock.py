#http://codeforces.com/problemset/problem/991/D
#Greedy Approach

"""
Bishwocks
XX   XX   .X   X.
X.   .X   XX   XX


00X00X0XXX0
0XXX0X00X00
"""

board=[]
for i in range(2):
	row=list(input())
	board.append(row)


n=len(row)

empty={}

"""
Solve it in terms of empty cells in i and i+1th column

empty(i) can be 0,1 or 2

Case 0,0:  MOVE ON!
Case 0,1:  keep track of that one empty cell
Case 0,2:  keep track of those two empty cells

Case 1,0: MOVE ON!
Case 1,1: keep track of that one empty cell
Case 1,2: ans++ 

Case 2,0: MOVE ON!
Case 2,1: ans++ 
Case 2,2: ans++ and keep track of that one cell

"""

for i in range(n):
	if(board[0][i]=='0' and board[1][i]=='0'):
		empty[i]=2 
	elif(board[0][i]=='0' or board[1][i]=='0'):
		empty[i]=1
	elif(board[0][i]=='X' and board[1][i]=='X'):
		empty[i]=0 

uec=0 #useful_empty_cell
bish=0

for i in range(n):
	current=empty[i]
	uec+=current
	if(uec>=3):
		uec-=3 
		bish+=1
	else:
		uec=current #abandom the previous empty cells 

	
print(bish)