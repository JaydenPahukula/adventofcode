from sys import stdin
from collections import defaultdict
data = [x.replace('\n','') for x in stdin.readlines()]

la,lb = [],defaultdict(int)
for line in data:
    a,b = line.split()
    la.append(int(a))
    lb[int(b)] += 1

count = 0
for a in la:
    count += a*lb[a]

print(count)
