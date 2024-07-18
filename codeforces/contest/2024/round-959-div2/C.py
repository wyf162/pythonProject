# -*- coding : utf-8 -*-
# @Time: 2024/7/18 22:55
# @Author: yefei.wang
# @File: C.py

import sys
from itertools import accumulate
import bisect

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
    n, x = MI()
    A = LI()
    PA = list(accumulate(A, initial=0))
    f = [0] * n

    for i in range(n - 1, -1, -1):
        i1 = bisect.bisect_right(PA, PA[i] + x)
        if i < i1 <= n:
            f[i] += 1 + (f[i1] if i1 < n else 0)
    # print(f)
    ans = n * (n + 1) // 2 - sum(f)
    print(ans)
