# -*- coding : utf-8 -*-
# @Time: 2024/3/22 22:55
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
    nums = LI()
    nums.sort()
    i = (n + 1) // 2 - 1
    med = nums[i]
    ans = 0
    while i < n and nums[i] == med:
        ans += 1
        i += 1
    print(ans)
