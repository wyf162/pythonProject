# -*- coding : utf-8 -*-
# @Time: 2024/6/12 1:07
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    x, y, z, k = MI()
    ans = 0
    for x1 in range(1, x + 1):
        for y1 in range(1, y + 1):
            if k % (x1 * y1) == 0:
                z1 = k // (x1 * y1)
                if z1 <= z:
                    # print(x1, y1, z1)
                    ans = max(ans, (x - x1 + 1) * (y - y1 + 1) * (z - z1 + 1))
    print(ans)
