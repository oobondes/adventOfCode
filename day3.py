#this script solves the problem here ----> https://adventofcode.com/2021/day/3
import sys
inp = sys.argv[1]

with open(inp,'r') as file:
    lines = file.readlines()

lngth = len(lines[0])-1
halfLngth = len(lines)//2
tracker = [0 for i in range(lngth)]
gamma = [0 for i in range(lngth)]
epsilon = [0 for i in range(lngth)]

for l in lines:
    for i in range(lngth):
        if l[i] == '1': 
            tracker[i] += 1
print('tracker: ',*tracker)
for i in range(lngth):
    if tracker[i] <= halfLngth:
        gamma[i] = '0'
        epsilon[i] = '1'
    else:
        gamma[i] = '1'
        epsilon[i] = '0'

print('gamma: ',*gamma,'\n','epsilon: ',*epsilon)

g = int(''.join(gamma),2)
e = int(''.join(epsilon),2)

print(f'ans: {e*g}')


