#this script solves the problem here ----> https://adventofcode.com/2021/day/11
import sys

inp = sys.argv[1]
points = list()
xmax = 0
ymax = 0
fold = list()
#read in file here
with open(inp,'r') as file:
    while True:
        pts = file.readline().split(',')
        print(pts)
        if pts == ['\n']: break
        x = int(pts[0])
        y = int(pts[1])
        if x > xmax: xmax = x
        if y > ymax: ymax = y
        points.append([x,y])
        print('::::',points[-1])
    fl = file.readlines()
    for f in fl:
        k,v = f[11::].split('=')
        fold.append([k,int(v)])

#create original set of points
paper = [[False for i in range(xmax+1)] for j in range(ymax+1)]
for x,y in points:
    paper[y][x] = True

print(*paper, sep='\n')

for dir, line in fold:
    if dir == 'y':
        print('y')
        tmp = list()
        for i in range(line):
            paper[i] = paper[i] and paper[2*line-1]
        paper = paper[:line]

    if dir == 'x':
        print('x')

print(*paper, sep='\n')