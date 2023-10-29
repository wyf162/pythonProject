# -*- coding : utf-8 -*-
# @Time: 2023/10/24 20:15
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

d = []
for i in range(1, n):
    d.append(a[i] - a[i-1])

ans = a[-1] - a[0]
d.sort()
while k > 1:
    v = d.pop()
    ans -= v
    k -= 1
print(ans)
