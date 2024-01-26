# -*- coding : utf-8 -*-
# @Time: 2024/1/26 19:06
# @Author: yefei.wang
# @File: B.py

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
for _tcn_ in range(tcn):
    n, m, p = MI()
    if n == 1:
        print('YangQiShaoNian')
        continue
    if p == 0:
        print('XiaoNian')
    elif p == 1:
        if n <= m + 1:
            print('XiaoNian')
        else:
            print('YangQiShaoNian')
