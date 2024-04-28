# -*- coding : utf-8 -*-
# @Time: 2024/4/28 22:41
# @Author: yefei.wang
# @File: E.py

import sys

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

n, m = MI()
xy = [LI() for i in range(n)]
dp0 = dict()
dp1 = dict()
dp0[0] = 0

for i in range(n):
    x, y = xy[i]
    ndp0 = dict()
    ndp1 = dict()
    for k in dp1:
        if k + x in ndp1:
            ndp1[k + x] = min(ndp1[k + x], dp1[k] + y)
        else:
            ndp1[k + x] = dp1[k] + y

    for k in dp0:
        if k + x in ndp0:
            ndp0[k + x] = min(ndp0[k + x], dp0[k] + y)
        else:
            ndp0[k + x] = dp0[k] + y

        if k + 2 * x in ndp1:
            ndp1[k + 2 * x] = min(ndp1[k + 2 * x], dp0[k] + y // 2)
        else:
            ndp1[k + 2 * x] = dp0[k] + y // 2
    for k in dp0:
        if k in ndp0:
            ndp0[k] = min(ndp0[k], dp0[k])
        else:
            ndp0[k] = dp0[k]

    for k in dp1:
        if k in ndp1:
            ndp1[k] = min(ndp1[k], dp1[k])
        else:
            ndp1[k] = dp1[k]
    dp0 = ndp0
    dp1 = ndp1

ans = 1 << 64
for k, v in dp0.items():
    if k >= m:
        ans = min(ans, v)

for k, v in dp1.items():
    if k >= m:
        ans = min(ans, v)
print(ans)
