import random

f = open('TeamNames.txt')
names = []
i = 0

for line in f:
    i += 1
    names.append(line)

j = random.randint(0, i-1)

print "Your team name is: " + names[j]
