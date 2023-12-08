# -*- coding : utf-8 -*-
# @Time: 2023/11/11 20:03
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

ss = {1, 11, 2, 22, 3, 33, 4, 44, 5, 55, 6, 66, 7, 77, 8, 88, 9, 99}

n = I()
d = LI()
rst = 0
for i in range(1, n+1):
    if i not in ss:
        continue
    x1 = i % 10
    x2 = x1 * 10 + x1
    if x1 <= d[i-1]:
        rst += 1
    if x2 <= d[i-1]:
        rst += 1
print(rst)
