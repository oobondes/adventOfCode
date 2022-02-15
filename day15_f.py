#this script solves the problem here ----> https://adventofcode.com/2021/day/15
import sys
import random

inp = sys.argv[1]
with open(inp,'r') as file:
    map = [[int(x) for x in line.strip()] for line in file.readlines()]
print(*map)
print('done')
map = [m + [(x+1)%10 if (x+1)%10 > 0  else (x+1)%10+1 for x in m] + [(x+2)%10 if (x+2)%10 > 1  else (x+2)%10+1 for x in m] + [(x+3)%10 if (x+3)%10 > 2  else (x+3)%10+1 for x in m] + [(x+4)%10 if (x+4)%10 > 3  else (x+4)%10+1 for x in m] for m in map]
map = map + [[(x+1)%10 if (x+1)%10 > 0  else (x+1)%10+1 for x in m] for m in map] + [[(x+2)%10 if (x+2)%10 > 1  else (x+2)%10+1 for x in m] for m in map] + [[(x+3)%10 if (x+3)%10 > 2  else (x+3)%10+1 for x in m] for m in map] + [[(x+4)%10 if (x+4)%10 > 3  else (x+4)%10+1 for x in m] for m in map]

x_last = len(map[0])-1
y_last = len(map)-1
paths = [[0,1,map[1][0]], [1,0,map[0][1]]]
minimum = 9999
print(minimum,'here!!!!!!!!!')
prev = dict()
dst = dict()
q = list()
for y in range(len(map)):
    for x in range(len(map[0])):
        prev[f'{x},{y}'] = ''
        dst[f'{x},{y}'] = 99999
        q.append(f'{x},{y}')
dst['0,0'] = map[0][0]
print(q)
sorted(q, key=lambda x: dst[x])
while q:
    u = q[0]
    del q[0]
    x,y = [int(i) for i in u.split(',')]
    for pt in [[x+1,y],[x,y+1]]:#,[x-1,y],[x,y-1]]:
        if 0<=pt[0]<=x_last and 0<=pt[1]<=y_last and f'{pt[0]},{pt[1]}' in q:
            alt = dst[u] + map[pt[1]][pt[0]]
            v=f'{pt[0]},{pt[1]}'
            if alt < dst[v]:
                dst[v] = alt
                prev[v] = u
    #sorted(q, key=lambda x: dst[x])
ans = dst[f'{x_last},{y_last}'] - map[0][0]
print('ans: ',ans)


dives = [{'x':0,'y':1,'val':0,'visited':['0-0'],'ended':False},{'x':1,'y':0,'val':0,'visited':['0-0'],'ended':False}]
while True:
    break
    l = len(dives)
    rng = l#l//10 if l >= 100 else l
    for i in range(rng):
        if dives[i]['ended']:
            print('ended')
            continue
        #if over lower risk path
        if dives[i]['val'] + map[dives[i]['y']][dives[i]['x']] >=  minimum:
            dives[i]['val'] += minimum
            continue
        #if endpoint
        if dives[i]['x'] == x_last and dives[i]['y'] == y_last:
            print('end')
            print(f'\n{minimum}\n')
            dives[i]['ended'] = True
            if map[dives[i]['y']][dives[i]['x']] + dives[i]['val'] < minimum:
                minimum = dives[i]['val'] + map[dives[i]['y']][dives[i]['x']]
                dives[i]['val']=minimum
            else:
                dives[i]['val'] += minimum
            dives[i]['val'] += map[dives[i]['y']][dives[i]['x']] + dives[i]['val']
            continue
        if f'{dives[i]["x"]}-{dives[i]["y"]}' in dives[i]['visited']:
            dives[i]['val'] += minimum
            continue
        else:
            dives[i]['visited'].append(f'{dives[i]["x"]}-{dives[i]["y"]}')
        for pt in [[dives[i]['x'],dives[i]['y']+1],[dives[i]['x']+1,dives[i]['y']]]:#,[dives[i]['x'],dives[i]['y']-1],[dives[i]['x']-1,dives[i]['y']]
            if 0<=pt[0]<=x_last and 0<=pt[1]<=y_last and f'{pt[0]}-{pt[1]}' not in dives[i]['visited']:
                dives.append({'x':pt[0],'y':pt[1],'val':dives[i]['val']+map[dives[i]['y']][dives[i]['x']],'visited':dives[i]['visited'].copy(),'ended':False})
    dives = [x for x in dives[rng:] if x['val'] <= minimum]
    tmp = list()
    #random.shuffle(dives) 
    dives = sorted(dives,key=lambda x: x['x']+x['y'],reverse= True)
    #dives = sorted(dives,key=lambda x: len(x['visited']),reverse=True)
    print(minimum)
    print(l)
    print(len(dives[0]['visited']))
    if len(dives) <= 1:
        ans = minimum
        #breakpoint()
        break
    


def dive(mp,x,y,endx,endy,visited, val):
    global minimum
    if val + mp[y][x] >=  minimum:
        return 999
    if x == endx and y == endy:
        if mp[y][x] + val < minimum:
            minimum = val + mp[y][x]
        else:
            return 9999999
        return mp[y][x] + val
    if f'{x}-{y}' in visited:
        return 999999999
    else:
        visited.append(f'{x}-{y}')
    srt = [(mp[pt[1]][pt[0]],pt) for pt in [[x,y+1],[x+1,y]] if 0<=pt[0]<=endx and 0<=pt[1]<=endy]#,[x-1,y],[x,y-1]
    srt = sorted(srt, key=lambda h: h[0],reverse=True)
    dives = [dive(mp,d[1][0],d[1][1],endx,endy,visited.copy(), val + mp[y][x]) for d in srt]
    return min(dives)

print(*map, sep  = '\n')
print('ans: ',ans)