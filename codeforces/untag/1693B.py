# -*- coding : utf-8 -*-
# @Time: 2024/1/30 21:00
# @Author: yefei.wang
# @File: 1693B.py

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    fa = [-1] + LGMI()
    left, right = [], []
    for _ in range(n):
        l, r = MI()
        left.append(l)
        right.append(r)

    deg = [0] * n
    for x, y in enumerate(fa):
        if y < 0:
            continue
        deg[y] += 1
    q = deque(i for i, d in enumerate(deg) if d == 0)
    dfs = []
    while q:
        x = q.popleft()
        dfs.append(x)
        deg[fa[x]] -= 1
        if deg[fa[x]] == 0:
            q.append(fa[x])
    # print(dfs)

    op = 0
    mi = [0] * n
    mx = [0] * n
    for y in dfs:
        if mx[y] < left[y]:
            op += 1
            x = fa[y]
            mx[x] += right[y] - mi[y]
            mi[x] += left[y] - mx[y]
        if mi[y] > right[y]:
            op += 1
            x = fa[y]

        else:
            x = fa[y]
            mi[x] += mi[y]
            mx[x] += mx[y]
    print(op)
