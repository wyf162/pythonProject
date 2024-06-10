# -*- coding : utf-8 -*-
# @Time: 2024/6/9 23:03
# @Author: yefei.wang
# @File: C2.py

import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    acc = list(accumulate(A, initial=0))
    mi = min(acc)
    if mi < 0:
        ans = 0
        cur = 0
        cnt = 0
        for i in range(n):
            cur += A[i]
            if cur == mi:
                ans += pow(2, cnt + n - i - 1, mod)
                ans %= mod
            cnt += int(cur >= 0)
    else:
        ans = pow(2, n, mod)
    print(ans)
