# -*- coding : utf-8 -*-
# @Time: 2024/4/13 22:53
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    mtx = [[0 for _ in range(n)] for _ in range(n)]
    ops = []

    for i in range(n):
        ops.append([1, n - i] + list(range(1, n + 1)))
        for r in range(n):
            mtx[n - i - 1][r] = r + 1

        ops.append([2, n - i] + list(range(1, n + 1)))
        for c in range(n):
            mtx[c][n - i - 1] = c + 1

    # for i in range(n):
    #     print(*mtx[i])

    tot = sum(sum(row) for row in mtx)
    cnt = len(ops)
    print(tot, cnt)
    for i in range(cnt):
        print(*ops[i])
