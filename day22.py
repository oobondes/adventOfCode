#this script solves the problem here ----> https://adventofcode.com/2021/day/17
import sys

cubes = [[[0 for x in range(101)] for y in range(101)] for z in range(101)]
inp = sys.argv[1]
with open(inp,'r') as file:
    for line in file:
        pos, ranges= line.split(' ')
        pos = 1 if pos == 'on' else 0
        x_range, y_range, z_range = ranges.split(',')
        x_range = x_range.split('=')[1].split('..')
        x_range = (int(x_range[0]),int(x_range[1])+1)
        if x_range[0] >51 or x_range[1] <-51:
            continue
        x_range = (x_range[0] if x_range[0] >= -51 else -51, x_range[1] if x_range[1] <= 51 else 51)
        y_range = y_range.split('=')[1].split('..')
        y_range = (int(y_range[0]),int(y_range[1])+1)
        y_range = (y_range[0] if y_range[0] >= -51 else -51, y_range[1] if y_range[1] <= 51 else 51)
        if y_range[0] >51 or y_range[1] <-51:
            continue
        z_range = z_range.split('=')[1].split('..')
        z_range = (int(z_range[0]),int(z_range[1])+1)
        z_range = (z_range[0] if z_range[0] >= -51 else -51, z_range[1] if z_range[1] <= 51 else 51)
        if z_range[0] >51 or z_range[1] <-51:
            continue
        print(pos,x_range,y_range,z_range)
        for x in range(*x_range):
            for y in range(*y_range):
                for z in range(*z_range):
                    cubes[z][y][x] = pos

    sum = 0
    for x in cubes:
        for y in x:
            for i in y:
                sum += i
print(sum)