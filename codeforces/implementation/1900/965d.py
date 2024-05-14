# -*- coding: utf-8 -*-
# @Time: 2024/5/14 11:00
# @Author: yfwang
# @File: 965d.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    w, l = MI()
    nums = LI()
    cur = sum(nums[:l])
    ans = cur

    for i in range(w-1-l):
        cur -= nums[i]
        cur += nums[i+l]
        ans = min(ans, cur)
    print(ans)