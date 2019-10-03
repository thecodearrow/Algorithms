import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	

def takeInput():
    return [int(x) for x in input().strip().split()]
 