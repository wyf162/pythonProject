# -*- coding : utf-8 -*-
# @Time: 2023/12/3 16:43
# @Author: yefei.wang
# @File: I.py

import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

tcn = I()

for _tnc_ in range(tcn):
    n = I()
    s = input()
    if s[n-1] in 'DB':
        print(0)
        continue
    c = 0
    for i in range(n - 1):
        if s[i] != 'B':
            c += 1
    rst = pow(2, c) - 1
    print(rst)
