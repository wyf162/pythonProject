# -*- coding : utf-8 -*-
# @Time: 2024/7/20 22:52
# @Author: yefei.wang
# @File: B.py

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
    n, x, y = MI()
    A = [1] * n

    for i in range(y - 2, -1, -1):
        A[i] = 0 - A[i + 1]

    for i in range(x, n, 1):
        A[i] = 0 - A[i - 1]
    print(*A)

    PA = [0] * n
    PA[0] = A[0]
    for i in range(1, n):
        PA[i] = PA[i - 1] + A[i]

    SA = [0] * n
    SA[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        SA[i] = SA[i + 1] + A[i]
    print(PA)
    print(SA)

    mx1 = max(PA)
    s1 = {i + 1 for i in range(n) if PA[i] == mx1}
    mx2 = max(SA)
    s2 = {i + 1 for i in range(n) if SA[i] == mx2}

    print(x, s1)
    print(y, s2)

    print(x in s1 and y in s2)
