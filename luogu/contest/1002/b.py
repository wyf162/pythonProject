# -*- coding : utf-8 -*-
# @Time: 2023/10/2 14:10
# @Author: yefei.wang
# @File: b.py


import sys

sys.stdin = open('../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, p = MI()
    if p > ((n - 1) // 2):
        print(-1)
    else:
        s = '101' + '01' * (p - 1)
        s = '0' * (n - len(s)) + s
        print(s)
