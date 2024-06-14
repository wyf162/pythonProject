# -*- coding: utf-8 -*-
# @Time: 2024/6/14 15:48
# @Author: yfwang
# @File: 1980F1.py

import sys
from collections import defaultdict

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

tcn = I()
for _tcn_ in range(tcn):
    n, m, k = MI()
    points = [LI() for _ in range(k)]
    groups = defaultdict(list)
    for i in range(k):
        r, c = points[i]
        groups[r].append(c)

    rs = list(sorted(groups.keys()))
    for r in rs:
        groups[r].sort()

    alpha = 0
    cur = n
    y = m
    vis = set()
    for r in rs[::-1]:
        alpha += (cur - r) * y
        cur = r
        if groups[r][0] - 1 < y:
            y = groups[r][0] - 1
            vis.add((r, groups[r][0]))
    alpha += (cur - 0) * y
    ans = [0] * k
    for i in range(k):
        r, c = points[i]
        if (r, c) in vis:
            ans[i] = 1
    print(alpha)
    print(*ans)


