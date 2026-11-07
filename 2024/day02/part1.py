from sys import stdin
data = [x.replace('\n','') for x in stdin.readlines()]

def check(report):
    n = len(report)
    if report[0] > report[1]:
        for i in range(1,n-1):
            if report[i] < report[i+1]: return False
    else:
        for i in range(1,n-1):
            if report[i] > report[i+1]: return False
    for i in range(n-1):
        d = abs(report[i]-report[i+1])
        if d < 1 or d > 3: return False
    return True

count = 0
for line in data:
    report = list(map(int, line.split()))
    if (check(report)):
        count += 1
    else:
        for i in range(len(report)):
            if check(report[:i] + report[i+1:]):
                count += 1
                break
print(count)
