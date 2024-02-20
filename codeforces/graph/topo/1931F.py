# https://codeforces.com/contest/1931/problem/F
# -*- coding : utf-8 -*-
# @Time: 2024/2/19 21:02
# @Author: yefei.wang
# @File: 1931F.py

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, k = MI()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(k):
        nums = LGMI()
        for i in range(2, n):
            x, y = nums[i - 1], nums[i]
            g[x].append(y)
            deg[y] += 1

    q = deque(i for i, d in enumerate(deg) if d == 0)
    topo_sort = []
    while q:
        x = q.popleft()
        topo_sort.append(x)
        for y in g[x]:
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
    YN(len(topo_sort) == n)
