# -*- coding : utf-8 -*-
# @Time: 2023/11/19 23:03
# @Author: yefei.wang
# @File: C.py

import math
import sys

sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m, k = MI()
