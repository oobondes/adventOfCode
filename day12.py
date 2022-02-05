#this script solves the problem here ----> https://adventofcode.com/2021/day/12
import graphlib
import sys


#graph class to store all connections from one point to another.
class graph:
    count = 0
    def __init__(self, val,next=None):
        self.count += 1
        self.val = val
        self.start = val == 'start'
        self.end = val == 'end'
        self.upper = val.isupper()
        self.lower = val.islower()
        if next != None:
            self.next = [next]
            next.addRT(self)
        else:
            self.next = list()
    def addRT(self,next):
        self.next.append(next)
        next.next.append(self)
    def getNext(self):
        return self.next

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    paths = [x.strip().split('-') for x in file.readlines()]

#adds all points to graph class
points = dict()
for stop in paths:
    if stop[0] not in points.keys():
        hd = graph(stop[0])
        if stop[1] not in points.keys():
            tail = graph(stop[1])
            hd.addRT(tail)
            points[stop[0]] = hd
            points[stop[1]] = tail
        else:
            hd.addRT(points[stop[1]])
            points[stop[0]] = hd
    else:
        if stop[1] not in points.keys():
            tail = graph(stop[1])
            tail.addRT(points[stop[0]])
            points[stop[1]] = tail
        else:
            points[stop[0]].addRT(points[stop[1]])
#sets head to the 'start' element
head = points['start']

#recursive method to explore paths
depth = len(points)
def findpaths(gr, visited, dep):
    if gr.end:
        print(*visited, 'end') 
        return 1
    if gr.lower and gr.val in visited:
        return 0
    if dep > depth+5:
        return 0
    visited.append(gr.val)
    ret = 0
    print(dep,':',gr.val)
    for x in gr.next:
        print(f'{dep}\t',x.val)
        print(len(x.next), f'dep:{dep} visited{visited}')
        ret += findpaths(x,visited[:],dep +1)
    return ret#sum([findpaths(x,visited,dep +1) for x in gr.next])


ans = findpaths(head, [], 1)
print(f'answer: {ans}')