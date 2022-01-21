lineSegments = list()
xmax, ymax = 0,0
with open('day5.txt','r') as file:
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
print(xmax,ymax,plot,sep='\n')
for set1, set2 in lineSegments:
    print(set1,set2)
    if set1[0] == set2[0]:
        if set1[1] > set2[1]:
            y1,y2 = set2[1],set1[1]
        else:
            y1,y2 = set1[1],set2[1]
        for y in range(y1,y2+1):
            plot[y][set1[0]] += 1
    if set1[1] == set2[1]:
        if set1[0] > set2[0]:
            x1,x2 = set2[0],set1[0]
        else:
            x1,x2 = set1[0],set2[0]
        for x in range(x1,x2+1):
            print(x, '-',set1[1])
            plot[set1[1]][x] += 1
for line in plot:
    print(line)

tot = 0
for line in plot:
    for x in line:
        if x >= 2:tot+=1
print(tot)

