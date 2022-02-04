#this script solves the problem here ----> https://adventofcode.com/2021/day/2
import sys
inp = sys.argv[1]

with open(inp,'r') as file:
    moves = file.readlines()

forward = 0
down = 0

for m in moves:
    direction, dist = m.split(' ')
    dist = int(dist)
    if direction == 'forward':
        forward += dist
    elif direction ==  'down':
        down += dist
    elif direction == 'up':
        down -= dist

print(f'forward: {forward}\ndown: {down}\nposition is :{forward*down}')
