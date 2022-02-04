#this script solves the problem here ----> https://adventofcode.com/2021/day/7
import sys

def factorial(x):
    if x == 0:
        return 0
    sum = 0
    while x >= 1:
        sum += x
        x -= 1
    return sum

inp = sys.argv[1]
with open(inp,'r') as file:
    positions = file.readlines()
positions = [int(p) for p in positions[0].split(',') if p]
positions.sort()

fuel = 99999999999

for p in range(positions[0],positions[-1]+1):
    f = [factorial(abs(p-x)) for x in positions]
    f = sum(f)
    if f < fuel:
        fuel = f
print('fuel: ',fuel)
