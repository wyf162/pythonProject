import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

YES = 'Yes'
NO = 'No'

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    s = sum(a)
    if s % n:
        print(NO)
        continue

    power_diff = Counter()
    for i in range(32):
        for j in range(32):
            power_diff[(1 << i) - (1 << j)] = (i, j)

    avg = s // n
    gives = [0] * 32
    receives = [0] * 32
    ans = True
    hst = Counter()
    for i in range(n):
        d = a[i] - avg
        if d in power_diff:
            x, y = power_diff[d]
            gives[x] += 1
            receives[y] += 1
        else:
            ans = False
            break
    if gives != receives:
        ans = False

    if ans:
        print(YES)
    else:
        print(NO)
