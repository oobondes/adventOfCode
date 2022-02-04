#this script solves the problem here ----> https://adventofcode.com/2021/day/1
import sys
#reads in the given argument to open the file with the input for this puzzle
inp = sys.argv[1]
with open(inp,'r') as file:
    measurements = file.readlines()

measurements = [int(m) for m in measurements if m]
#loops through the measurments, 3 at a time, to see if the next sliding window of three have increased or not.
increases = 0
for i in range(1,len(measurements)-2):
    if sum(measurements[i:i+3]) > sum(measurements[i-1:i+2]): increases += 1

print(f'The measurement increased {increases} times')
