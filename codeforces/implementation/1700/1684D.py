# -*- coding : utf-8 -*-
# @Time: 2023/10/19 19:33
# @Author: yefei.wang
# @File: 1684D.py

import sys

import copy

# sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    b = copy.deepcopy(a)
    while k:
        m = len(b)
        mx = 0
        j = -1
        for i in range(m):
            if m - 1 - i - b[i] <= mx:
                mx = m - 1 - i - b[i]
                j = i
        c = []
        for i in range(m):
            if i < j:
                c.append(b[i])
            elif i > j:
                c.append(b[i]+1)
        b = c
        k -= 1
    ans = sum(b)
    print(ans)
