# -*- coding : utf-8 -*-
# @Time: 2023/11/4 10:21
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    a.sort()
    a[1] += 1
    a.sort()
    rst = sum(a[1:-1])
    print(rst)
