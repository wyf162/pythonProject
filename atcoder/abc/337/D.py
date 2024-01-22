# -*- coding : utf-8 -*-
# @Time: 2024/1/20 20:21
# @Author: yefei.wang
# @File: G.py

import sys

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

h, w, k = MI()
grid = [list(input()) for _ in range(h)]
rst = h * w + 1

for i in range(h):
    a = [0]
    for j in range(w):
        if grid[i][j] == 'x':
            a = [0]
        else:
            if grid[i][j] == 'o':
                a.append(a[-1] + 1)
            else:
                a.append(a[-1])
            if len(a) > k:
                rst = min(rst, k - (a[-1] - a[-k-1]))

for j in range(w):
    a = [0]
    for i in range(h):
        if grid[i][j] == 'x':
            a = [0]
        else:
            if grid[i][j] == 'o':
                a.append(a[-1] + 1)
            else:
                a.append(a[-1])
            if len(a) > k:
                rst = min(rst, k - (a[-1] - a[-k-1]))

if rst == h * w + 1:
    print(-1)
else:
    print(rst)
