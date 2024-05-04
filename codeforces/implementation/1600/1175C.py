# -*- coding : utf-8 -*-
# @Time: 2024/5/4 10:48
# @Author: yefei.wang
# @File: 1175C.py
# https://codeforces.com/problemset/problem/1175/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, k = MI()
    nums = LI()
    d = 0x3f3f3f3f
    ans = -1
    for i in range(n - k):
        d1 = (nums[i + k] - nums[i] + 1) // 2
        if d1 < d:
            d = d1
            ans = (nums[i + k] + nums[i]) // 2
    print(ans)
