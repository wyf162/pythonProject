# -*- coding : utf-8 -*-
# @Time: 2024/5/2 9:34
# @Author: yefei.wang
# @File: 213C.py

import sys
from math import inf

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
grid = [LI() for _ in range(n)]

f = [[-inf] * n for _ in range(n)]
f[0][0] = grid[0][0]
for k in range(1, n * 2 - 1):
    for x1 in range(min(k, n - 1), max(k - n, -1), -1):
        for x2 in range(min(k, n - 1), x1 - 1, -1):
            y1, y2 = k - x1, k - x2
            res = f[x1][x2]  # 都往右
            if x1:
                res = max(res, f[x1 - 1][x2])  # 往下，往右
            if x2:
                res = max(res, f[x1][x2 - 1])  # 往右，往下
            if x1 and x2:
                res = max(res, f[x1 - 1][x2 - 1])  # 都往下
            res += grid[x1][y1]
            if x2 != x1:  # 避免重复摘同一个樱桃
                res += grid[x2][y2]
            f[x1][x2] = res
print(f[-1][-1])
