# -*- coding : utf-8 -*-
# @Time: 2023/11/11 19:41
# @Author: yefei.wang
# @File: E.py

import math
import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
pre_sum = [0]
for i in range(n):
    pre_sum.append(pre_sum[-1] + a[i])


def check(x):
    k = 0
    i = 0
    while i < n:
        j = i + 1
        sm = 0
        while j < n and sm <= x:
            sm += a[j] * (pre_sum[j] - pre_sum[i])
            j += 1
        k += 1
        i = max(i + 1, j - 1)
    return k


ans = 1
l, r = 1, 100
while l <= r:
    mid = (l + r) // 2
    if check(mid) <= m:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
