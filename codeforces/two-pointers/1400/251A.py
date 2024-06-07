# -*- coding: utf-8 -*-
# @Time: 2024/5/13 9:08
# @Author: yfwang
# @File: 251A.py

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

tcn = 3
for _tcn_ in range(tcn):
    n, d = MI()
    nums = LI()
    nums.sort()
    i = 0
    ans = 0
    for j in range(n):
        while nums[j] - nums[i] > d:
            i += 1
        k = j - i
        ans += k * (k - 1) // 2
    print(ans)
