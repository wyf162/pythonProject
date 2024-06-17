# -*- coding : utf-8 -*-
# @Time: 2024/6/16 21:17
# @Author: yefei.wang
# @File: 1978D.py

import sys
from itertools import accumulate

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
    n, c = MI()
    A = LI()
    A[0] += c
    ans = [0] * n
    mx = max(A)
    j = A.index(mx)
    PA = list(accumulate(A, initial=0))
    for i in range(n):
        if PA[i + 1] >= mx:
            ans[i] = i
        else:
            ans[i] = i + 1
    ans[j] = 0
    print(*ans)
