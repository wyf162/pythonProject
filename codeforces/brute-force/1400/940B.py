# -*- coding: utf-8 -*-
# @Time: 2024/4/22 9:04
# @Author: yfwang
# @File: 940B.py

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
k = I()
A = I()
B = I()

if k == 1:
    ans = A * (n - 1)
    print(ans)
    exit()


h = []
heappush(h, (0, n))
while h:
    cost, x = heappop(h)
    if x == 1:
        ans = cost
        break
    if x % k == 0:
        mi = min(cost + B, cost + A * (x - x // k))
        heappush(h, (mi, x // k))
    else:
        c1, c2 = divmod(x, k)
        if c1 == 0:
            heappush(h, (cost + A * (x - 1), 1))
        else:
            heappush(h, (cost + A * c2, x - c2))

print(ans)
