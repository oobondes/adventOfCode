#this script solves the problem here ----> https://adventofcode.com/2021/day/17
import re
import sys
import numpy as np

num = re.compile('[\d]*')


inp = sys.argv[1]
with open(inp,'r') as file:
    size = max([int(y) for y in num.findall(''.join(file.readlines())) if y])#parses file for largest number
    cubes = np.zeros((size*2 +1,size*2 +1,size*2 +1))
    file.seek(0)
    for line in file:
        pos, ranges= line.split(' ')
        pos = 1 if pos == 'on' else 0
        x_range, y_range, z_range = ranges.split(',')
        x_range = x_range.split('=')[1].split('..')
        x_range = (int(x_range[0])+size,int(x_range[1])+size)
        y_range = y_range.split('=')[1].split('..')
        y_range = (int(y_range[0])+size,int(y_range[1])+size)
        z_range = z_range.split('=')[1].split('..')
        z_range = (int(z_range[0])+size,int(z_range[1])+size)
        print(pos,x_range,y_range,z_range)
        print(pos,x_range,y_range,z_range)
        for x in range(*x_range):
            for y in range(*y_range):
                for z in range(*z_range):
                    cubes[z][y][x] = pos

    sum = cubes.sum()
    print(sum)