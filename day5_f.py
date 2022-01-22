import sys

inp = sys.argv[1]
lineSegments = list()
xmax, ymax = 0,0
with open(inp,'r') as file:
    for line in file:
        if line == '\n':break
        coordinates = line.split('->')
        x1, y1 = coordinates[0].split(',')
        x2, y2 = coordinates[1].split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 > xmax: xmax = x1
        if x2 > xmax: xmax = x2
        if y1 > ymax: ymax = y1
        if y2 > ymax: ymax = y2
        lineSegments.append([[x1,y1],[x2,y2]])

plot = [[0 for x in range(xmax+1)] for i in range(ymax+1)]
for set1, set2 in lineSegments:
    if set1[0] == set2[0]:
        if set1[1] > set2[1]:
            y1,y2 = set2[1],set1[1]
        else:
            y1,y2 = set1[1],set2[1]
        for y in range(y1,y2+1):
            plot[y][set1[0]] += 1
    elif set1[1] == set2[1]:
        if set1[0] > set2[0]:
            x1,x2 = set2[0],set1[0]
        else:
            x1,x2 = set1[0],set2[0]
        for x in range(x1,x2+1):
            plot[set1[1]][x] += 1
    else:
        if set1[0] > set2[0] and set1[1] > set2[1]:
            x,y = set2[0],set2[1]
            while True:
                plot[y][x] += 1
                y+=1
                x+=1
                if set1 == [x-1,y-1]:break
        elif set1[0] > set2[0] and set1[1] < set2[1]:
            x,y = set2[0],set2[1]
            while True:
                plot[y][x] += 1
                y-=1
                x+=1
                if set1 == [x-1,y+1]:break
        elif set1[0] < set2[0] and set1[1] > set2[1]:
            x,y = set2[0],set2[1]
            while True:
                plot[y][x] += 1
                y+=1
                x-=1
                if set1 == [x+1,y-1]:break
        elif set1[0] < set2[0] and set1[1] < set2[1]:
            x,y = set1[0],set1[1]
            while True:
                plot[y][x] += 1
                y+=1
                x+=1
                if set2 == [x-1,y-1]:break

for line in plot:
    print(*line)

tot = 0
for line in plot:
    for x in line:
        if x >= 2:tot+=1
print(tot)

