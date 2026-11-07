from sys import stdin
data = [x.replace('\n','') for x in stdin.readlines()]

la,lb = [],[]
for line in data:
    a,b = line.split()
    la.append(int(a))
    lb.append(int(b))

la.sort()
lb.sort()

count = 0
for i in range(len(la)):
    count += abs(la[i]-lb[i])

print(count)
