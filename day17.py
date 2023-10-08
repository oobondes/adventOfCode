#this script solves the problem here ----> https://adventofcode.com/2021/day/17
from re import T
import sys

inp = sys.argv[1]
with open(inp,'r') as file:
    tmp = file.readline().strip().split(': ')[1].split(', ')
    xS,xE = [int(x) for x in tmp[0].split('=')[-1].split('..')]
    yS,yE = [int(x) for x in tmp[1].split('=')[-1].split('..')]
print(tmp)
print(xS,xE,yS,yE)

def inbounds(pt):
    global xS,xE,yS,yE
    if xS<=pt[0]<=xE and yS<=pt[1]<=yE:
        return True
    return False

def fact(x):
    if x == 1:
        return 1
    else:
        return x+fact(x-1)

ans = 0
