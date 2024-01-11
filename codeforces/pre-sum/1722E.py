# -*- coding : utf-8 -*-
# @Time: 2024/1/4 22:02
# @Author: yefei.wang
# @File: 1722E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n, q = MI()
    H, W = 1001, 1001
    mtx = [[0 for _ in range(W)] for _ in range(H)]
    for _ in range(n):
        h, w = MI()
        mtx[h][w] += 1

    pre_sum = [[0 for _ in range(W + 1)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            pre_sum[i][j + 1] = pre_sum[i][j] + i * mtx[i][j] * j

    for _ in range(q):
        hs, ws, hb, wb = MI()
        ret = 0
        for h in range(hs + 1, hb):
            ret += pre_sum[h][wb] - pre_sum[h][ws + 1]
        print(ret)
