# -*- coding: utf-8 -*-
# @Time: 2024/3/4 9:24
# @Author: yfwang
# @File: 650A.py
# https://codeforces.com/problemset/problem/650/A

import sys
from collections import Counter

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

n = I()
xs, ys, xy = [], [], []
for _ in range(n):
    x, y = MI()
    xs.append(x)
    ys.append(y)
    xy.append(x * 10 ** 10 + y)
xs.sort()
ys.sort()

c1 = Counter(xs)
c2 = Counter(ys)
c3 = Counter(xy)
ans = 0
for k, v in c1.items():
    ans += v * (v - 1) // 2
for k, v in c2.items():
    ans += v * (v - 1) // 2
for k, v in c3.items():
    ans -= v * (v - 1) // 2
print(ans)
