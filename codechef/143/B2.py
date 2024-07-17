# -*- coding : utf-8 -*-
# @Time: 2024/7/17 23:45
# @Author: yefei.wang
# @File: B2.py

import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../jury.txt', 'w')
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
    A.sort()
    i1 = 0
    ans = 0
    for i2 in range(n):
        while i1 < i2 and A[i2] - A[i1] > i2 - i1 + 1:
            i1 += 1

        for i3 in range(i1, i2):
            if 2 <= A[i2] - A[i3] <= i2 - i3 + 1:
                ans += math.comb(i2 - i3 - 1, A[i2] - A[i3] - 2)
            else:
                break

    print(ans)