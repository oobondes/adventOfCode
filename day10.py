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


points ={')': 3,']': 57,'}': 1197,">": 25137}
match = {'(':')','[':']','{':'}','<':'>'}


inp = sys.argv[1]
#read in file here
with open(inp,'r') as file:
    brackets = file.readlines()

ans = 0
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
                ans += points[c]
                break

print(ans)