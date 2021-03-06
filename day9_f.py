#this script solves the problem here ----> https://adventofcode.com/2021/day/9
import sys

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    lines = [x.strip() for x in file.readlines()]




lowpoints = list()

length = len(lines[0])
height = len(lines)
pts = list()
for i in range(len(lines)):
    lines[i] = [int(x) for x in list(lines[i])]

def findBasin(x,y):
    chkd = list()
    def helper(pnt):
        x1,y1 = pnt    
        
        if y1 >= height or x1 >= length or x1 < 0 or y1 < 0:
            return 0
        
        if f'{pnt[0]}-{pnt[1]}' in chkd: 
            return 0
        
        if lines[y1][x1] == 9:
            return 0
        
        chkd.append(f'{pnt[0]}-{pnt[1]}')
        return 1  + helper([x1-1,y1]) + helper([x1,y1-1]) + helper([x1,y1+1]) + helper([x1+1,y1])
    ans = helper([x,y])
    return ans


#check corners
if lines[0][0] < lines[0][1] and lines[0][0] < lines[1][0]: 
    lowpoints.append(lines[0][0])
    pts.append([0,0])
if lines[0][length-1] < lines[0][length-2] and lines[0][length-1] < lines[1][length-1]: 
    lowpoints.append(lines[0][length-1])
    pts.append([0,length-1])
if lines[height-1][0] < lines[height-2][0] and lines[height-1][0] < lines[height-1][1]: 
    lowpoints.append(lines[height-1][0])
    pts.append([height-1,0])
if lines[height-1][length-1] < lines[height-2][length-1] and lines[height-1][length-1] < lines[height-1][length-2]: 
    lowpoints.append(lines[height-1][length-1])
    pts.append([height-1,length-1])

#checks top and bottom
for i in range(1, length-1):
    if lines[0][i] < lines[0][i-1] and lines[0][i] < lines[0][i+1] and lines[0][i] < lines[1][i]:
        lowpoints.append(lines[0][i])
        pts.append([0,i])
    if lines[height-1][i] < lines[height-1][i-1] and lines[height-1][i] < lines[height-1][i+1] and lines[height-1][i] < lines[height-2][i]:
        lowpoints.append(lines[height-1][i])
        pts.append([height-1,i])
#check sides
for i in range(1, height-1):
    if lines[i][0] < lines[i-1][0] and lines[i][0] < lines[i+1][0] and lines[i][0] < lines[i][1]: 
        lowpoints.append(lines[i][0])
        pts.append([i,0])
    if lines[i][length-1] < lines[i-1][length-1] and lines[i][length-1] < lines[i+1][length-1] and lines[i][length-1] < lines[i][length-2]: 
        lowpoints.append(lines[i][length-1])
        pts.append([i,length-1])
 #check for the inside
for x in range(1,length-1):
    for y in range(1,height-1):
        if lines[y][x] < lines[y][x+1] and lines[y][x] < lines[y][x-1] and lines[y][x] < lines[y-1][x] and lines[y][x] < lines[y+1][x]:
            lowpoints.append(lines[y][x])
            pts.append([y,x])

ans = [findBasin(x[1],x[0]) for x in pts]
ans.sort()
print(f'ans: {ans[-1]*ans[-2]*ans[-3]}')