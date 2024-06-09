# -*- coding : utf-8 -*-
# @Time: 2024/6/9 9:54
# @Author: yefei.wang
# @File: 660D.py
# geometry

import sys
from collections import defaultdict

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

n = I()
points = [LI() for _ in range(n)]
ans = 0
hst = defaultdict(int)
N = 2 * 10 ** 9
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        x3, y3 = x1 + x2, y1 + y2
        idx = x3 * N + y3
        ans += hst[idx]
        hst[idx] += 1
print(ans)
