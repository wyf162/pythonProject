# -*- coding : utf-8 -*-
# @Time: 2023/12/8 19:11
# @Author: yefei.wang
# @File: B.py

import math
import sys

sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    c = LI()
    p = LI()

