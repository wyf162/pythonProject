# -*- coding: utf-8 -*-
# @Time: 2024/4/26 16:15
# @Author: yfwang
# @File: 1499C.py
# https://codeforces.com/contest/1499/problem/C

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
    n = I()
    nums = LI()
    tot0 = nums[0]
    mi0 = nums[0]
    tot1 = nums[1]
    mi1 = nums[1]
    ans = mi0 * n + mi1 * n
    for i in range(2, n):
        if i % 2 == 0:
            tot0 += nums[i]
            mi0 = min(mi0, nums[i])
            ans = min(ans, tot0 + mi0 * (n - i // 2 - 1) + tot1 + mi1 * (n - i // 2))
        else:
            tot1 += nums[i]
            mi1 = min(mi1, nums[i])
            ans = min(ans, tot0 + mi0 * (n - i // 2 - 1) + tot1 + mi1 * (n - i // 2 - 1))
    print(ans)
