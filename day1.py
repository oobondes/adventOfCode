#this script solves the problem here ----> https://adventofcode.com/2021/day/1
import sys
#reads the 1st command line argument, which should be the input file, and 
inp = sys.argv[1]
with open(inp,'r') as file:
    measurements = file.readlines()

measurements = [int(m) for m in measurements if m]

#loops through and counts how many times measurements increase from one reading to the next
increases = 0
for i in range(1,len(measurements)):
    if measurements[i] > measurements[i-1]: increases += 1

print(f'The measurement increased {increases} times')
