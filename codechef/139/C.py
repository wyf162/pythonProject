# -*- coding : utf-8 -*-
# @Time: 2024/6/19 22:57
# @Author: yefei.wang
# @File: C.py

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
    P = LI()
    f = [0] * n
    f[n - 1] = 1
    for i in range(n - 2, -1, -1):
        if P[i + 1] > P[i]:
            f[i] = 1
        else:
            break

    L = 1
    R = n
    ans = 1
    for i in range(1, n - 1):
        a, b, c = P[i - 1], P[i], P[i + 1]
        if a < b < c:
            continue
        if a > b > c:
            ans = 0
            break
        if a < b > c > a:
            L = max(L, b - c)
        if c < b > a > c:
            L = max(L, a - c)
            L = max(L, b - c)
        if a > b < c:
            L = max(L, a - b)
            if f[i] == 0:
                R = min(R, c - b)

    if ans == 0 or L > R:
        ans = 0
        print(ans)
    else:
        ans = (L + R) * (R - L + 1) // 2
        print(ans)
