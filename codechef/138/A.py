# -*- coding : utf-8 -*-
# @Time: 2024/6/12 22:30
# @Author: yefei.wang
# @File: A.py
import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    x, y = MI()
    t = math.ceil((10 * y - 10 * x) / (100 - y))
    print(t)
