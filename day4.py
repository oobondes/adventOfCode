#this script solves the problem here ----> https://adventofcode.com/2021/day/4
import sys
inp = sys.argv[1]



def check(b,l):
    for row in b:
        chk = [x in l for x in row]
        if False not in chk: 
            return True
    for i in range(0,5):
        chk = [b[x][i] in l for x in range(0,5)]
        if False not in chk: 
            return True
    #if (b[0][0] in l and b[1][1] in l and b[2][2] in l and b[3][3] in l and b[4][4] in l) or (b[4][0] in l and b[3][1] in l and b[2][2] in l and b[1][3] in l and b[0][4] in l):
     #   print('diag')
      #  return True
    return False
    
with open(inp,'r') as file:
	nums = [int(x) for x in file.readline().strip().split(',')]
	lines = file.readlines()

board = list()    
for t in lines:
	if t=='\n':
		board.append([])
		continue
	board[-1].append([int(x) for x in t.split(' ') if x != ''])

print(nums)
print(board)
for b in board:
	print(b)


called = list()
breakOuter = False
for n in nums:
	called.append(n)
	for b in board:
		if check(b,called):
			won = b
			breakOuter = True
			print('\n\n', won)
			break
	if breakOuter: break

sum = 0
for b in won:
	for x in b:
		if x not in called: sum += x
		
print(f'ans: {sum*called[-1]}')
