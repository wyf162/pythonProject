# -*- coding: utf-8 -*-
# @Time: 2024/6/3 9:10
# @Author: yfwang
# @File: 1873F.py

import sys
from itertools import accumulate
import bisect

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

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    A = LI()
    H = LI()
    PA = list(accumulate(A, initial=0))
    R = [n] * n
    for i in range(n - 2, -1, -1):
        if H[i] % H[i + 1] == 0:
            R[i] = R[i + 1]
        else:
            R[i] = i
    ans = 0
    for i in range(n):
        j = bisect.bisect_right(PA, PA[i] + k)
        # print(j - i - 1, R[i] - i + 1)
        bns = min(j - i - 1, R[i] - i + 1)
        ans = max(ans, bns)
    print(ans)
