#this script solves the problem here ----> https://adventofcode.com/2021/day/8
import sys

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    lines = file.readlines()
lines = [x.split(' | ')[-1].strip() for x in lines if x]
count = 0
print(*lines,sep='\n')
for line in lines:
    for word in line.split(' '):
        length = len(word)
        print(word)
        if length == 2 or length == 4 or length == 3 or length == 7:
            print(word)
            count += 1

print(count)
