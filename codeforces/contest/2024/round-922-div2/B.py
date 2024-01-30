# -*- coding : utf-8 -*-
# @Time: 2024/1/30 22:39
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    perm1 = LI()
    perm2 = LI()
    xy = [(x, y) for x, y in zip(perm1, perm2)]
    xy.sort()
    p1, p2 = [], []
    for x, y in xy:
        p1.append(x)
        p2.append(y)
    print(*p1)
    print(*p2)
