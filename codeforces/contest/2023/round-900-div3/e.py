# -*- coding : utf-8 -*-
# @Time: 2023/9/26 23:24
# @Author: yefei.wang
# @File: e.py


import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()

for _tcn_ in range(tcn):
    n = I()
    a = LI()
    q = I()
    qs = [LI()+[i] for i in range(q)]
    qs.sort()
    ans = []
    v = []
    j = n-1
    for l, k, i in qs:
        while l<j:
            v.append()