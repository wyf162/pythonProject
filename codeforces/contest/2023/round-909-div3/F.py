# -*- coding : utf-8 -*-
# @Time: 2023/11/18 12:23
# @Author: yefei.wang
# @File: F.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, q = MI()
    qs = [LI() for _ in range(q)]
    for i in range(n - 1):
        print(i + 1, i + 2)
    for i in range(q):
        print(-1, -1, -1)
