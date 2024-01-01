# -*- coding : utf-8 -*-
# @Time: 2023/12/30 22:32
# @Author: yefei.wang
# @File: A.py

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
    n, k = MI()
    b = LI()
    prd = 1
    for i in range(n):
        prd *= b[i]
    if 2023 % prd:
        print('NO')
    else:
        ret = [2023//prd] + [1] * (k-1)
        print('YES')
        print(*ret)
