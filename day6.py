import sys

infile = sys.argv[1]
with open(infile,'r') as file:
    lant = file.readlines()
lant = [int(i) for i in lant[0].split(',')]
days = 80

school = [0]*9
for i in lant:
    school[i] += 1

for i in range(days):
    newFish = school.pop(0)
    school.append(newFish)
    school[6] += newFish

    
print('total fish: ',sum(school))
