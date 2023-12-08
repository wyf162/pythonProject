# -*- coding : utf-8 -*-
# @Time: 2023/11/10 19:40
# @Author: yefei.wang
# @File: C2.py

import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

for i in range(100):
    n, m, x = MI()
    a = LI()
    b = LI()

    for k in range(n*m):
        i = k//m
        j = k % m
        s = [x, a[i], b[j]]
        s.sort()
        x = s[1]
    print(x)
    if x not in [a[-1], b[-1]]:
        print(a)
        print(b)
