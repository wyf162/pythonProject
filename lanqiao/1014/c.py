# -*- coding : utf-8 -*-
# @Time: 2023/10/14 19:15
# @Author: yefei.wang
# @File: c.py

import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()

a.sort()


def check(mid):
    pre = a[0]
    cnt = 1
    for i in range(1, n):
        if a[i] - pre <= mid:
            continue
        else:
            pre = a[i]
            cnt += 1
    return cnt <= k


l, r = 0, a[-1]
ans = r

while l <= r:
    m = (l + r) // 2
    if check(m):
        ans = m
        r = m - 1
    else:
        l = m + 1

print(ans)
