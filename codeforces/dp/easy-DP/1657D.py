# -*- coding: utf-8 -*-
# @Time: 2024/5/17 17:43
# @Author: yfwang
# @File: 1657D.py

import bisect
import sys
from collections import Counter

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
inf = 0x3f3f3f3f

tcn = 1
for _tcn_ in range(tcn):
    n, coins = MI()
    squads = [LI() for _ in range(n)]
    m = I()
    monsters = [LI() for i in range(m)]
    hst = Counter()
    for i in range(n):
        c, h, d = squads[i]
        hst[c] = max(hst[c], h * d)
    f = [0] * (coins + 1)
    for k, v in hst.items():
        c = 1
        while k * c <= coins:
            f[k * c] = max(f[k * c], v * c)
            c += 1
    for i in range(1, coins + 1):
        f[i] = max(f[i], f[i - 1])

    # print(f)
    ans = [-1] * m
    for i in range(m):
        j = bisect.bisect_right(f, monsters[i][0] * monsters[i][1])
        if j <= coins:
            ans[i] = j
    print(*ans)
