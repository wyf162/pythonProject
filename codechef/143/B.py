# -*- coding : utf-8 -*-
# @Time: 2024/7/17 22:50
# @Author: yefei.wang
# @File: B.py

import math
import sys
from itertools import accumulate

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

N = 2 * 10 ** 5
acc = list(accumulate(range(N)))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    A.sort()
    i1 = 0
    ans = 0
    last_gap = -1
    for i2 in range(n):
        if i2 >= 1 and A[i2] - A[i2 - 1] == 2:
            last_gap = i2
        while i1 < i2 and A[i2] - A[i1] > i2 - i1 + 1:
            i1 += 1
        if 2 <= A[i2] - A[i1] <= i2 - i1 + 1:
            if last_gap >= 0 and last_gap > i1:
                ans += last_gap - i1
                if i2 - last_gap - 1 > 0:
                    ans += acc[i2 - last_gap - 1]
            else:
                ans += acc[i2 - i1 - 1]
    print(ans)
