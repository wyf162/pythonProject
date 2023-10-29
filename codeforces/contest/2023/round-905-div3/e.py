# -*- coding : utf-8 -*-
# @Time: 2023/10/22 20:05
# @Author: yefei.wang
# @File: e.py

import sys
import math

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = [math.log2(x) for x in a]
    ops = 0
    for i in range(1, n):
        if b[i] >= b[i-1]:
            continue
        else:
            op = math.ceil(b[i-1] - b[i])
            ops += op
            b[i] += op
    print(ops)
