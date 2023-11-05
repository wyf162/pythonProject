# -*- coding : utf-8 -*-
# @Time: 2023/10/29 23:27
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()
a.sort()
if k >= n:
    exit(print(0))

pre_sum = [0]
for i in range(n):
    pre_sum.append(pre_sum[-1] + a[i])

rst = a[-1] - a[0]
for i in range(k+1):
    j = k - i
    s = pre_sum[i] + pre_sum[-1] - pre_sum[-j-1]
    avg = s/k
    rst_t = max(a[-j-1] - a[i], abs(a[-j-1] - avg), abs(avg - a[i]))
    rst = min(rst, rst_t)

print(rst)
