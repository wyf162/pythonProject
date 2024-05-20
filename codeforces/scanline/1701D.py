# -*- coding : utf-8 -*-
# @Time: 2024/5/20 20:29
# @Author: yefei.wang
# @File: 1701D.py
# https://codeforces.com/contest/1701/problem/D

import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
inf = 10 ** 9

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    b = LI()
    upper = [0] * n
    lower = [0] * n
    for i in range(n):
        if b[i] == 0:
            upper[i] = n
            lower[i] = i + 1 + 1
        else:
            upper[i] = (i + 1) // b[i]
            lower[i] = (i + 1 + b[i] + 1) // (b[i] + 1)
    add = [[] for _ in range(n)]
    for i, (l, r) in enumerate(zip(lower, upper)):
        add[l - 1].append((r, i))
    ans = [-1] * n
    hq = []
    for i in range(n):
        for tmp in add[i]:
            heappush(hq, tmp)
        _, j = heappop(hq)
        ans[j] = i + 1
    print(*ans)
