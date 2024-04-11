# -*- coding : utf-8 -*-
# @Time: 2024/4/10 22:49
# @Author: yefei.wang
# @File: B.py

import sys
from math import inf

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    if n <= 2:
        print('Bob')
        continue
    elif n == 3:
        print('Alice')
        continue
    if n % 2 == 0:
        print('Alice')
    else:
        print('Bob')

