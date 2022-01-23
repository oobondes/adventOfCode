import sys

inp = sys.argv[1]
with open(inp,'r') as file:
    measurements = file.readlines()

measurements = [int(m) for m in measurements if m]

increases = 0
for i in range(1,len(measurements)-2):
    if sum(measurements[i:i+3]) > sum(measurements[i-1:i+2]): increases += 1

print(f'The measurement increased {increases} times')
