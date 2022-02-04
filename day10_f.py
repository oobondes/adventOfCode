#this script solves the problem here ----> https://adventofcode.com/2021/day/10
import sys
def isOpen(s):
    if s in "[{(<":
        return True
    else:
        return False
def isClose(s):
    if s in ">}])":
        return True
    else:
        return False


points ={'(': 1,'[':2,'{': 3,"<": 4}
match = {'(':')','[':']','{':'}','<':'>'}


inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    brackets = file.readlines()

ans = list()
que = list()
for i, b in enumerate(brackets):
    que = list()
    for c in b:
        if isOpen(c):
            que.append(c)
        if isClose(c):
            if match[que[-1]] == c:
                que.pop()
            else:
                que = list()
                break
    que = que[::-1]
    if que:
        a = 0
        for c in que:
            a = a*5 + points[c]
        ans.append(a)

ans.sort()
print(ans[len(ans)//2])