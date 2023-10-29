# -*- coding : utf-8 -*-
# @Time: 2023/10/8 20:02
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()

for _tcn_ in range(tcn):
    n, x, y = input().split()
    n = int(n)
