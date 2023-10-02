# -*- coding : utf-8 -*-
# @Time: 2023/9/23 21:05
# @Author: yefei.wang
# @File: c.py
import sys

sys.stdin = open('../../../input.txt', 'r')
k = int(input())

a = []

for i in range(1, (1 << 10), 1):
    x = 0
    for j in range(9, -1, -1):
        if (i >> j) & 1:
            x = x * 10 + j
    a.append(x)
a.sort()
ans = a[k]
print(ans)
