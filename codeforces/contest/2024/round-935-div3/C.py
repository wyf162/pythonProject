# -*- coding: utf-8 -*-
# @Time: 2024/3/19 16:17
# @Author: yfwang
# @File: C.py


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
    nums = [int(x) for x in input()]
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + nums[i]

    if pre_sum[-1] * 2 >= n:
        ans = 0
    else:
        ans = -1

    for i in range(n):
        left_ok = i + 1 - (pre_sum[i + 1] - pre_sum[0])
        right_ok = pre_sum[-1] - pre_sum[i + 1]
        if left_ok * 2 >= i + 1 and right_ok * 2 >= (n - i - 1):
            if abs(n - (i + 1) * 2) < abs(n - ans * 2):
                ans = i + 1
    print(ans)
