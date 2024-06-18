# -*- coding: utf-8 -*-
# @Time: 2024/6/18 9:01
# @Author: yfwang
# @File: 976C.py
# sortings heapq

import sys
from collections import defaultdict
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
    groups = defaultdict(list)
    for i in range(n):
        L, R = MI()
        groups[L].append((R, i + 1))

    LS = list(sorted(groups.keys()))
    for L in LS:
        groups[L].sort()
        if len(groups[L]) >= 2:
            ans = (groups[L][0][1], groups[L][1][1])
            break
    else:
        h = []
        find = False
        ans = (-1, -1)
        for L in LS:
            if h:
                for R, i in groups[L]:
                    if R <= -h[0][0]:
                        ans = (i, h[0][1])
                        find = True
                        break
            if find:
                break
            for R, i in groups[L]:
                heappush(h, (-R, i))

    print(*ans)
