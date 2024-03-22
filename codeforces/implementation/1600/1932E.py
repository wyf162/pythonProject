# -*- coding: utf-8 -*-
# @Time: 2024/3/22 16:38
# @Author: yfwang
# @File: 1932E.py
# https://codeforces.com/problemset/problem/1932/E


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
    nums = [int(x) for x in input()]
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + nums[i]

    ans = []
    carry = 0
    for i in range(n):
        x = pre_sum[n - i] + carry
        carry = x // 10
        ans.append(x % 10)
    while carry:
        ans.append(carry % 10)
        carry = carry // 10
    while ans[-1] == 0:
        ans.pop()

    print(''.join(str(x) for x in ans[::-1]))
