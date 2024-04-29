# -*- coding : utf-8 -*-
# @Time: 2024/4/29 22:37
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
    nums = LGMI()
    ans = 3
    hst = dict()
    for i, p in enumerate(nums):
        if p in hst and hst[p] == i:
            ans = 2
        hst[i] = p
    print(ans)
