# -*- coding: utf-8 -*-
# @Time: 2024/5/17 17:43
# @Author: yfwang
# @File: 1657D.py

import sys

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

tcn = 3
for _tcn_ in range(tcn):
    n, coins = MI()
    squads = [LI() for _ in range(n)]
    m = I()
    monsters = [[i] + LI() for i in range(m)]
    ans = [inf] * m
    squads.sort(key=lambda x: x[1] * x[2])
    monsters.sort(key=lambda x: x[1] * x[2])
    j = n - 1
    mi = inf
    for i in range(m-1, -1, -1):
        while j >= 0 and squads[j][1] * squads[j][2] > monsters[i][1] * monsters[i][2]:
            mi = min(inf, squads[j][0])
            j -= 1
        idx = monsters[i][0]
        ans[idx] = mi
    ans = [x if x < inf else -1 for x in ans]
    print(*ans)


