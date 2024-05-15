# -*- coding : utf-8 -*-
# @Time: 2024/5/15 21:12
# @Author: yefei.wang
# @File: 1651D.py
# https://codeforces.com/contest/1651/problem/D
# manhattan

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


def manht(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


inf = 0x3f3f3f3f

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    points = [TI() for _ in range(n)]
    hst = dict()
    dis = dict()
    for x, y in points:
        hst[(x, y)] = None
        dis[(x, y)] = inf
    q = deque()

    for x, y in points:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in hst:
                hst[(x, y)] = nx, ny
                dis[(nx, ny)] = 1
                break
        else:
            q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if hst[(nx, ny)]:
                if dis[(x, y)] > manht(x, y, *hst[(nx, ny)]):
                    hst[(x, y)] = hst[(nx, ny)]
                    dis[(x, y)] = manht(x, y, *hst[(nx, ny)])
        if dis[(x, y)] == inf:
            q.append((x, y))

    ans = [hst[(x, y)] for x, y in points]
    for i in range(n):
        print(*ans[i])
