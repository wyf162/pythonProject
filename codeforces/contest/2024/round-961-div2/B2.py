# -*- coding : utf-8 -*-
# @Time: 2024/7/23 22:56
# @Author: yefei.wang
# @File: B2.py

import sys

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
    n, m = MI()
    A = LI()
    C = LI()

    idxs = sorted(range(n), key=lambda i: A[i])

    ans = 0
    for i in range(n):
        i1 = idxs[i]
        ans = max(ans, min(m // A[i1], C[i1]) * A[i1])

    for i in range(n - 1):
        i1, i2 = idxs[i], idxs[i + 1]
        if A[i1] + 1 != A[i2]:
            continue
        tot = A[i1] * C[i1] + A[i2] * C[i2]
        if tot <= m:
            ans = max(ans, tot)
            continue

        m1 = A[i1] * C[i1]
        m2 = A[i2] * C[i2]
        if m1 >= m:
            r1 = m - m // A[i1] * A[i1]
            ans = max(ans, m - max(r1 - min(C[i2], C[i1]), 0))
        else:
            m3 = m - m1
            c2 = min(m3 // A[i2], C[i2])
            r1 = m3 - c2 * A[i2]
            ans = max(ans, m - max(r1 - min(C[i2] - c2, C[i1]), 0))

    print(ans)
