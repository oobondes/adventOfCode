#this script solves the problem here ----> https://adventofcode.com/2021/day/7
import sys

inp = sys.argv[1]
with open(inp,'r') as file:
    positions = file.readlines()
positions = [int(p) for p in positions[0].split(',')if p]
fuel = 99999999999

for p in positions:
    f = sum([abs(p-x) for x in positions])
    if f < fuel:
        fuel = f
print('fuel: ',fuel)
