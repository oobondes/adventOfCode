#this script solves the problem here ----> https://adventofcode.com/2021/day/14
import sys
from pprint import pprint
inp = sys.argv[1]
replacement = dict()
with open(inp,'r') as file:
    text = file.readline().strip()
    file.readline() #gets rid of empty line
    while True:
        tmp = file.readline()
        if tmp == '\n' or tmp == '':break
        tmp = tmp.strip().split(' -> ')
        left_expansion = f"{tmp[0][0]}{tmp[1]}"
        right_expansion = f"{tmp[1]}{tmp[0][1]}"
        replacement[tmp[0].strip()] = {'next_count':0,'count':0,'replacements':[left_expansion,right_expansion],'added_letter':tmp[1]}

for i,c in enumerate(text[:-1]):
    replacement[text[i:i+2]]['count'] += 1
pprint(replacement)
cycles = 40
letters = {c:text.count(c) for c in set(''.join(replacement.keys()))}
print('='*20)
for _ in range(cycles):
    for letter in replacement:
        for n_letter in replacement[letter]['replacements']:
            replacement[n_letter]['next_count'] += replacement[letter]['count']
        if replacement[letter]['count']:
            letters[replacement[letter]['added_letter']] += replacement[letter]['count']
    for letter in replacement:
        replacement[letter]['count'], replacement[letter]['next_count'] = replacement[letter]['next_count'],0
    # pprint(letters)
pprint(replacement)    

# letters = {c:0 for c in set(''.join(replacement.keys()))}
# for key in replacement:
#     for letter in key:
#         letters[letter] += replacement[key]['count']
print(letters)
print(f"ans: {max(letters.values()) - min(letters.values())}")

