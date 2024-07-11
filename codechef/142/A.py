# -*- coding : utf-8 -*-
# @Time: 2024/7/10 22:29
# @Author: yefei.wang
# @File: A.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    ans = n - A.count(0)
    for i in range(32):
        x = (1 << i) - 1
        c = v = 0
        for a in A:
            if a > x:
                c += 1
            else:
                v |= a
        if v == x:
            ans = min(ans, c)
    print(ans)
