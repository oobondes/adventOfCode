#this script solves the problem here ----> https://adventofcode.com/2021/day/9
import sys

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    lines = [x.strip() for x in file.readlines()]



lowpoints = list()

length = len(lines[0])
height = len(lines)
for i in range(len(lines)):
    lines[i] = [int(x) for x in list(lines[i])]

for x in lines:
    print(*x, sep='')

#check corners
if lines[0][0] < lines[0][1] and lines[0][0] < lines[1][0]: lowpoints.append(lines[0][0])
if lines[0][length-1] < lines[0][length-2] and lines[0][length-1] < lines[1][length-1]: lowpoints.append(lines[0][length-1])
if lines[height-1][0] < lines[height-2][0] and lines[height-1][0] < lines[height-1][1]: lowpoints.append(lines[height-1][0])
if lines[height-1][length-1] < lines[height-2][length-1] and lines[height-1][length-1] < lines[height-1][length-2]: lowpoints.append(lines[height-1][length-1])

#checks top and bottom
for i in range(1, length-1):
    if lines[0][i] < lines[0][i-1] and lines[0][i] < lines[0][i+1] and lines[0][i] < lines[1][i]:
        lowpoints.append(lines[0][i])
    if lines[height-1][i] < lines[height-1][i-1] and lines[height-1][i] < lines[height-1][i+1] and lines[height-1][i] < lines[height-2][i]:
        lowpoints.append(lines[height-1][i])
#check sides
for i in range(1, height-1):
    if lines[i][0] < lines[i-1][0] and lines[i][0] < lines[i+1][0] and lines[i][0] < lines[i][1]: 
        lowpoints.append(lines[i][0])
    if lines[i][length-1] < lines[i-1][length-1] and lines[i][length-1] < lines[i+1][length-1] and lines[i][length-1] < lines[i][length-2]: 
        lowpoints.append(lines[i][length-1])
 #check for the inside
for x in range(1,length-1):
    for y in range(1,height-1):
        if lines[y][x] < lines[y][x+1] and lines[y][x] < lines[y][x-1] and lines[y][x] < lines[y-1][x] and lines[y][x] < lines[y+1][x]:
            lowpoints.append(lines[y][x])
            print(f'{x+1},{y+1}    {lines[y][x]}')
            print('----',lines[y+1][x+1],lines[y+1][x-1],lines[y-1][x+1],lines[y-1][x-1])

print(*lowpoints, sep=', ')
ans = sum([x + 1 for x in lowpoints])
print(f'ans: {ans}')