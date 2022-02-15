#this script solves the problem here ----> https://adventofcode.com/2021/day/14
import sys

inp = sys.argv[1]
replacement = dict()
with open(inp,'r') as file:
    text = file.readline().strip()
    file.readline() #gets rid of empty line
    while True:
        tmp = file.readline()
        if tmp == '\n' or tmp == '':break
        tmp = tmp.strip().split('->')
        replacement[tmp[0].strip()] = tmp[1].strip()

cycles = 10

def polymer(txt, depth):
    if depth == 0:
        return ''
    return ''
    

for i in range(cycles):
    j = len(text) +1
    while j > 0:
        if text[j-2:j] in replacement.keys():
            text = text[:j-1] + replacement[text[j-2:j]] + text[j-1:]
        j  -= 1
    print(i)

letters = ''.join([x for x in replacement.keys() if x != '\n'])
count = dict()
for char in letters:
    if char not in count.keys():
        count[char] = 0
for char in text:
    count[char] += 1
count = [count[v] for v in count]
m = max(count)
mi = min(count)


print(m-mi)
    
