# -*- coding : utf-8 -*-
# @Time: 2024/1/27 14:53
# @Author: yefei.wang
# @File: 1469C.py

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
inf = float('inf')

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    h = LI()
    low, high = h[0], h[0] + k
    ans = True
    for i in range(1, n):
        low = max(low - k + 1, h[i])
        high = min(high + k - 1, h[i] + k - 1 + k)
        if high - low < k:
            ans = False
            break
    ans &= low == h[-1]
    YN(ans)
