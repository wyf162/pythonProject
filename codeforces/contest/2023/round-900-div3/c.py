# -*- coding : utf-8 -*-
# @Time: 2023/9/26 22:55
# @Author: yefei.wang
# @File: c.py
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()

for _tcn_ in range(tcn):
    n, k, x = MI()
    mi = (1+k)*k // 2
    mx = (n+n-k+1)*k // 2
    if mi <= x <= mx:
        print('YES')
    else:
        print('NO')