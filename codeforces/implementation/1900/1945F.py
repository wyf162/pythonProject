# -*- coding : utf-8 -*-
# @Time: 2024/6/30 12:08
# @Author: yefei.wang
# @File: 1945F.py

import sys
from heapq import heappop, heappush

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
    n = I()
    A = LI()
    P = LGMI()
    h = []
    ans = 0
    p = -1
    for i in range(n - 1, -1, -1):
        heappush(h, A[P[i]])
        while len(h) > i + 1:
            heappop(h)
        r = h[0] * len(h)
        if r >= ans:
            ans = r
            p = i + 1
    print(ans, p)
