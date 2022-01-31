import sys

def contains9(l):
    for row in l:
        for x in row:
            if 10 <= x < 100:
                return True
    return False

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    lines = [x.strip() for x in file.readlines()]
lines = [[int(x) for x in l] for l in lines]
cycles = 0
height = len(lines)
length = len(lines[0])
flashCount = 0

while True:
    lines = [[x+1 for x in l] for l in lines]

    while contains9(lines):
        for x in range(length):
            for y in range(height):
                #print(f'{x},{y}')
                if 100 > lines[y][x] > 9:
                    lines[y][x] = 100
                    flashCount += 1
                    print(flashCount)
                    try:
                        lines[y+1][x] += 1
                    except:pass
                    try:
                        lines[y+1][x+1] += 1
                    except:pass
                    try:
                        if x-1 >= 0:
                            lines[y+1][x-1] += 1
                    except:pass
                    try:
                        if y-1 >= 0:
                            lines[y-1][x] += 1
                    except:pass
                    try:
                        if y-1 >= 0:
                            lines[y-1][x+1] += 1
                    except:pass
                    try:
                        if x-1 >= 0 and y-1 >= 0:
                            lines[y-1][x-1] += 1
                    except:pass
                    try:
                        lines[y][x+1] += 1
                    except:pass
                    try:
                        if x-1 >= 0:
                            lines[y][x-1] += 1
                    except:pass
    lines = [[x if x<100 else 0 for x in l] for l in lines]
    cycles += 1
    test = []
    for row in lines:
        for x in row:
            test.append(x == 0)
    if False not in test:
        break
    

print(*lines, sep='\n')
print('ans: ',cycles)