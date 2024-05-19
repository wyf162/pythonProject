# -*- coding : utf-8 -*-
# @Time: 2024/5/19 16:43
# @Author: yefei.wang
# @File: 1661D.py

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

tcn = 1
for _tcn_ in range(tcn):
    n, k = MI()
    b = LI()

    currsum = 0
    start = [0] * n
    currcnt = 0
    for i in range(n - 1, k - 1, -1):
        b[i] -= currsum
        needed = (b[i] - 1) // k + 1
        if needed < 0:
            needed = 0
        b[i] -= needed * k
        start[i - k + 1] = needed
        currcnt += needed
        currsum += k * needed
        currsum -= currcnt
        currcnt -= start[i]
    # print(start, b)
    for i in range(k - 1, -1, -1):
        b[i] -= currsum
        currsum -= currcnt
        currcnt -= start[i]
    big = 0
    for i in range(k):
        big = max(big, (b[i] - 1) // (i + 1) + 1)
    print(sum(start) + big)
