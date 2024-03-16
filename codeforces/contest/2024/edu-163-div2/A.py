# -*- coding : utf-8 -*-
# @Time: 2024/3/15 22:35
# @Author: yefei.wang
# @File: A.py

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
    n = I()
    if n % 2:
        print("NO")
    else:
        print("YES")
        t = "AABB"
        if n % 4:
            ret = 'CC' + t * (n // 4)
        else:
            ret = t * (n // 4)
        print(ret)
