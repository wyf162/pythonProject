# -*- coding : utf-8 -*-
# @Time: 2024/2/19 23:32
# @Author: yefei.wang
# @File: F.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
N = 7
for _tcn_ in range(tcn):
    grid = [list(input()) for _ in range(N)]