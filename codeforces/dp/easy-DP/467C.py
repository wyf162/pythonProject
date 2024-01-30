# -*- coding : utf-8 -*-
# @Time: 2023/10/10 21:55
# @Author: yefei.wang
# @File: 467C.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
pre_sum = [0] * (n + 1)
for i in range(n):
    pre_sum[i + 1] = pre_sum[i] + a[i]

f = [[0 for j in range(k + 1)] for i in range(n)]

for i in range(n):
    for j in range(k):
        if i - m + 1 >= 0:
            f[i][j] = max(f[i - 1][j], f[i - m][j - 1] + pre_sum[i + 1] - pre_sum[i - m + 1])

rst = max(max(f[i]) for i in range(n))
print(rst)
