#this script solves the problem here ----> https://adventofcode.com/2021/day/12
import graphlib
import sys

class graph:
    count = 0
    def __init__(self, val,next=None):
        self.count += 1
        self.val = val
        if next != None:
            self.next = [next]
            next.addRT(self)
        else:
            self.next = list()
    def addRT(self,next):
        self.next.append(next)
    def getNext(self):
        return self.next

inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    paths = {x.split('-')[0]:x.split('-')[0] for x in file.readlines()}
head = graph('start', graph('end'))
print(head.val)
print(head.next[0].val)

print(paths)