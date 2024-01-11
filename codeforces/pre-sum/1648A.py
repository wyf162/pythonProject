import sys
from collections import defaultdict

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n, m = MI()
mtx = [LI() for i in range(n)]

rst = 0
hst = defaultdict(list)
for i in range(n):
    for j in range(m):
        hst[mtx[i][j]].append(i)

for k, v in hst.items():
    v.sort()
    s = v[0]
    for i in range(1, len(v)):
        rst += v[i] * i - s
        s += v[i]


hst = defaultdict(list)
for i in range(n):
    for j in range(m):
        hst[mtx[i][j]].append(j)

for k, v in hst.items():
    v.sort()
    s = v[0]
    for i in range(1, len(v)):
        rst += v[i] * i - s
        s += v[i]

print(rst)
