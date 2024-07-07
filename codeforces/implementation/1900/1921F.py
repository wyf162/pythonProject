# -*- coding : utf-8 -*-
# @Time: 2024/7/7 9:33
# @Author: yefei.wang
# @File: 1921F.py
# https://codeforces.com/problemset/problem/1921/F

import sys

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
    n, q = MI()
    A = LI()
    groups = [[] for _ in range(n + 1)]
    for i in range(q):
        s, d, k = MI()
        groups[d].append((s - 1, k, i))
    ans = [0] * q

    K = min(n, 500)
    for d in range(n, K, -1):
        for s, k, j in groups[d]:
            for i in range(k):
                ans[j] += A[s] * (i + 1)
                s += d

    B = [0] * (n + K + 5)
    C = [0] * (n + K + 5)
    for d in range(K, 0, -1):
        if not groups[d]:
            continue
        for i in range(n + K + 5):
            B[i] = 0
            C[i] = 0
        for i in range(n):
            B[i + d] = B[i] + A[i] * (i // d + 1)
            C[i + d] = C[i] + A[i]

        for s, k, j in groups[d]:
            ans[j] = B[s + k * d] - B[s] - (C[s + k * d] - C[s]) * (s // d)

    print(*ans)
