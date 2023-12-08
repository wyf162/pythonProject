# -*- coding : utf-8 -*-
# @Time: 2023/12/2 20:10
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()

b = sorted(a)

s = sum(b)
hst = dict()
for i in range(n):
    hst[b[i]] = s
    hst[b[i]] -= b[i]
    s -= b[i]
rst = [0] * n
for i in range(n):
    rst[i] = hst[a[i]]
print(*rst)


