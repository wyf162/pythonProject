# -*- coding : utf-8 -*-
# @Time: 2023/10/14 13:16
# @Author: yefei.wang
# @File: 1608C.py

import sys
from heapq import heappop, heapify

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = LI()
    ai = [(-x, i) for i, x in enumerate(a)]
    bi = [(-x, i) for i, x in enumerate(b)]
    heapify(ai)
    heapify(bi)
    xa, ia = heappop(ai)
    xb, ib = heappop(bi)
    winner = [0] * n
    winner[ia] = 1
    winner[ib] = 1

    mia = min(a[ia], a[ib])
    mib = min(b[ia], b[ib])

    for i in range(2*n+2):
        while ai and -ai[0][0] > mia:
            xa, ia = heappop(ai)
            mib = min(mib, b[ia])
            mia = min(mia, a[ia])
            winner[ia] = 1

        while bi and -bi[0][0] > mib:
            xb, ib = heappop(bi)
            mia = min(mia, a[ib])
            mib = min(mib, b[ib])
            winner[ib] = 1

    print(''.join(map(str, winner)))
