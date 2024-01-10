# -*- coding : utf-8 -*-
# @Time: 2023/12/1 18:56
# @Author: yefei.wang
# @File: B.py
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, x, y = MI()
    p = LI()
    p.sort()
    if n == 1:
        rst = min(p[0] * x / 100, max(p[0] - y, 0))
    else:
        s = sum(p[:-2])
        rst = min(
            s + p[-1] * x / 100 + max(p[-2] - y, 0),
            s + p[-2] * x / 100 + max(p[-1] - y, 0), )
    print(rst)
