#this script solves the problem here ----> https://adventofcode.com/2021/day/3
import sys
inp = sys.argv[1]

with open(inp,'r') as file:
    lines = file.readlines()

lngth = len(lines[0])-1
halfLngth = len(lines)//2
oxygen = ''
co2 = ''

for i in range(lngth):
    oxygen_1 = 0
    oxygen_0 = 0
    co2_1 = 0
    co2_0 = 0
    ox = list()
    co = list()
    for line in lines:
        if line.startswith(oxygen):
            ox.append(line)
            if line[i] == '1':
                oxygen_1 += 1
            else:
                oxygen_0 += 1
        if line.startswith(co2):
            co.append(line)
            if line[i] == '1':
                co2_1 += 1
            else:
                co2_0 += 1
    if oxygen_1 >= oxygen_0:
         oxygen += '1'
    else:
         oxygen += '0'
    if co2_1 < co2_0:
         co2 += '1'
    else:
         co2 += '0'
    if len(ox) == 1:
        oxygen = ox[0]
    if len(co) == 1:
        co2 = co[0]

o = int(oxygen, 2)
c = int(co2, 2)
print('oxygen: ',oxygen, ' - ', o)
print('co2: ', co2, ' - ', c)
print(f'answer is {c*o}')
