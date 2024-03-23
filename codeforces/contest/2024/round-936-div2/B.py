# -*- coding : utf-8 -*-
# @Time: 2024/3/22 23:02
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
    n, k = MI()
    nums = LI()
    mx = -10 ** 9
    tot = 0
    for i in range(n):
        tot += nums[i]
        mx = max(mx, tot)
        tot = max(tot, 0)
    if mx <= 0:
        ret = sum(nums) % mod
    else:
        ret = mx * (1 << k) % mod
        ret += sum(nums) - mx
        ret %= mod
    print(ret)
