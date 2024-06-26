# -*- coding : utf-8 -*-
# @Time: 2024/6/26 22:47
# @Author: yefei.wang
# @File: C.py

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    g = [[] for _ in range(n)]
    deg = [0 for _ in range(n)]
    for i in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    mi = min(A)
    idx = A.index(mi)
    q = deque()
    unvis = [1] * n
    for i, d in enumerate(deg):
        if i != idx and d == 1:
            q.append(i)
            unvis[i] = 0
    rets = []
    while q:
        x = q.popleft()
        rets.append(x)
        for y in g[x]:
            deg[y] -= 1
            if y != idx and unvis[y] and deg[y] == 1:
                q.append(y)
    print(n-1)
    print(*[x+1 for x in rets])