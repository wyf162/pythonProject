# -*- coding: utf-8 -*-
# @Time: 2024/3/25 15:24
# @Author: yfwang
# @File: 1964D.py
# https://codeforces.com/problemset/problem/1946/D

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
    n, x = MI()
    nums = LI()

    xor = 0
    for i in range(n):
        xor ^= nums[i]
    if xor > x:
        print(-1)
        continue
    ans = 0
    for b in range(31, -1, -1):
        mask = 1 << b
        if xor & mask == 0:
            group = []
            v = 0
            for i in range(len(nums)):
                v ^= nums[i]
                if v & mask == 0:
                    group.append(v)
                    v = 0
            if x & mask != 0:
                ans = max(ans, len(group))
            else:
                nums = group
        else:
            if x & mask == 0:
                break
    else:
        ans = max(ans, len(nums))

    print(ans)
