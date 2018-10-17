import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass
	