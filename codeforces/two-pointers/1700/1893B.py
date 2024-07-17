# -*- coding: utf-8 -*-
# @Time: 2024/7/17 9:54
# @Author: yfwang
# @File: 1893B.py
import sys

from algorithms.dp import longest_increasing_subsequence_optimized2

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
    n, m = MI()
    A = LI()
    B = LI()
    g = [[] for _ in range(n + 1)]
    B.sort(reverse=True)
    indices = sorted(range(n), key=lambda i: -A[i])
    indices.append(n)
    i1, i2 = 0, 0
    while i2 < m:
        # print(i1, i2)
        if i1 >= n or B[i2] >= A[indices[i1]]:
            g[indices[i1]].append(B[i2])
            i2 += 1
        else:
            i1 += 1

    C = []
    for i in range(n):
        for x in g[i]:
            C.append(x)
        C.append(A[i])
    for x in g[n]:
        C.append(x)
    print(*C)
    lis = longest_increasing_subsequence_optimized2(C)
    print(lis, end=' ')
    lis = longest_increasing_subsequence_optimized2(A)
    print(lis)
