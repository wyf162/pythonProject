# -*- coding: utf-8 -*-
# @Time: 2024/2/21 10:07
# @Author: yfwang
# @File: 1920C.py
# https://codeforces.com/problemset/problem/1920/C

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


def gcd(m, n):
    while n != 0:
        m, n = n, m % n

    return m


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    ans = 0
    for i in range(1, n + 1):
        if n % i:
            continue
        k = i
        x = 0
        for i in range(0, n - k):
            y = abs(nums[i + k] - nums[i])
            if y == 0:
                continue
            x = gcd(x, y)
            if x == 1:
                break
        ans += (x != 1)
    print(ans)
