# -*- coding : utf-8 -*-
# @Time: 2023/12/3 14:41
# @Author: yefei.wang
# @File: D.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()

grid = [LI() for i in range(n)]
w = b = 0
mx = 0
for i in range(n):
    odd, event = 0, 0
    for j in range(n):
        if (i + j) % 2 == 0:
            w += grid[i][j]
        else:
            b += grid[i][j]
        if j % 2 == 0:
            event += grid[i][j]
        else:
            odd += grid[i][j]
    mx = max(mx, abs(odd - event))

rst = w - b + mx

print(rst)
