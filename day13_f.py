#this script solves the problem here ----> https://adventofcode.com/2021/day/13
import sys

def printlist(l):
    print('='*len(l[0]))
    for row in l:
        for item in row:
            if item:
                print('*',end='')
            else:
                print('.',end='')
        print('')
    print('='*len(l[0]))

inp = sys.argv[1]
points = list()
xmax = 0
ymax = 0
fold = list()
#read in file here
with open(inp,'r') as file:
    while True:
        pts = file.readline().split(',')
        if pts == ['\n']: break
        x = int(pts[0])
        y = int(pts[1])
        if x > xmax: xmax = x
        if y > ymax: ymax = y
        points.append([x,y])
    fl = file.readlines()
    for f in fl:
        k,v = f[11::].split('=')
        fold.append([k,int(v)])

ymax+=1
xmax+=1
if fold[0][0] == 'y':
    ymax = 2*fold[0][1]+1
else:
    xmax = 2*fold[0][1]+1
if fold[1][0] == 'y':
    ymax = 2*fold[1][1]+1
else:
    xmax = 2*fold[1][1]+1
    
#create original set of points
paper = [[False for i in range(xmax)] for j in range(ymax)]
for x,y in points:
    paper[y][x] = True


for dir, line in fold:
    if dir == 'y':
        for y in range(line):
            for x in range(xmax):
                paper[y][x] = paper[y][x] or paper[2*line-y][x]
        paper = paper[:line]
        ymax = line
    if dir == 'x':
        for y in range(ymax):
            for x in range(line):
                try:
                    paper[y][x] = paper[y][x] or paper[y][2*line-x]
                except IndexError:
                    
                    print(f'x:{x},y:{y},line:{line},test:{2*line-x}')
                    exit()
        paper = [row[:line] for row in paper]
        xmax = line
    ans = sum([sum([1 for i in row if i == True]) for row in paper])
    
printlist(paper)
