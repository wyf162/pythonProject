# -*- coding : utf-8 -*-
# @Time: 2024/1/10 19:24
# @Author: yefei.wang
# @File: 1677A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    ans = 0
    ctr_less_than_c = [0] * n
    for bi in range(n):
        b = nums[bi]
        d_counter = 0
        for ci in range(n - 1, bi, -1):
            c = nums[ci]
            ans += ctr_less_than_c[c] * d_counter
            if b > c:
                d_counter += 1
            else:
                ctr_less_than_c[c] += 1
    print(ans)
