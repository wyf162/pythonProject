# -*- coding : utf-8 -*-
# @Time: 2024/6/9 22:55
# @Author: yefei.wang
# @File: C.py

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
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    acc = list(accumulate(A, initial=0))
    mi = min(acc)
    if mi < 0:
        ans = acc[-1] - mi * 2
    else:
        ans = acc[-1]
    print(ans)
