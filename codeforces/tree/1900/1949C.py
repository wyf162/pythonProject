# -*- coding : utf-8 -*-
# @Time: 2024/6/30 9:30
# @Author: yefei.wang
# @File: 1949C.py
# trees

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for i in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    cnt = [1] * n
    h = []
    for i in range(n):
        if deg[i] == 1:
            heappush(h, (cnt[i], i))

    while h:
        _, x = heappop(h)
        for y in g[x]:
            if cnt[y] >= cnt[x]:
                cnt[y] += cnt[x]
                cnt[x] = 0
                deg[y] -= 1
                if deg[y] == 1:
                    heappush(h, (cnt[y], y))
    if n in cnt:
        YN(True)
    else:
        YN(False)

