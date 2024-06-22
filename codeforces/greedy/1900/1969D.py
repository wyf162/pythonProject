# -*- coding : utf-8 -*-
# @Time: 2024/6/22 14:55
# @Author: yefei.wang
# @File: 1969D.py
# sortings greedy

import sys
from heapq import heappush, heappop

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
    n, k = MI()
    A = LI()
    B = LI()

    C = [(a, b) for a, b in zip(A, B)]
    C.sort(key=lambda x: -x[1])
    f = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        a, b = C[i]
        f[i] = f[i+1] + max(b - a, 0)
    h = []
    tot = 0
    for i in range(k):
        heappush(h, -C[i][0])
        tot += C[i][0]
    ans = 0
    ans = max(ans, f[k] - tot)
    for i in range(k, n):
        heappush(h, -C[i][0])
        tot += C[i][0]
        tot += heappop(h)
        ans = max(ans, f[i+1] - tot)
    print(ans)
