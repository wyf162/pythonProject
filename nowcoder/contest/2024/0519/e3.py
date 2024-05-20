# -*- coding : utf-8 -*-
# @Time: 2024/5/19 20:53
# @Author: yefei.wang
# @File: e3.py

import math
import sys
from collections import defaultdict

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

n = I()
xs = []
ys = []
for _ in range(n):
    x, y = MI()
    xs.append(x)
    ys.append(y)

ans = -1

vis = defaultdict(list)
for i in range(n):
    for j in range(i):
        vis[(xs[i] + xs[j], ys[i] + ys[j])].append((xs[i] - xs[j], ys[i] - ys[j]))

for x in vis.values():
    if len(x) > 1:
        k = len(x)
        for i in range(k):
            dx1, dy1 = x[i]
            for j in range(i):
                dx2, dy2 = x[j]
                if dx1 * dy2 != dx2 * dy1:
                    ans = max(ans, abs(dx1 * dy2 - dy1 * dx2) // 2)

if ans == -1:
    print(-1)
else:
    print(str(ans) + '.0')
