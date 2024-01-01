# -*- coding : utf-8 -*-
# @Time: 2023/12/30 23:45
# @Author: yefei.wang
# @File: D.py

import sys

sys.stdin = open('./../../../input.txt')
input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    pass