# -*- coding : utf-8 -*-
# @Time: 2023/11/7 22:56
# @Author: yefei.wang
# @File: C.py

import sys
from collections import Counter

sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
