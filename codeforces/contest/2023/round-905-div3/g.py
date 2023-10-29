# -*- coding : utf-8 -*-
# @Time: 2023/10/22 19:52
# @Author: yefei.wang
# @File: g.py

import sys
from collections import Counter
from heapq import heappop, heappush

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')


tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    a = LI()
    b = LI()
