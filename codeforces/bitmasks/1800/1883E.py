# -*- coding: utf-8 -*-
# @Time: 2024/2/27 9:55
# @Author: yfwang
# @File: 1883E.py
# https://codeforces.com/problemset/problem/1883/E

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


def compute(a, b):
    if a < b:
        i = 0
        while True:
            if (a << i) <= b:
                ans = i
            else:
                break
            i += 1
        return -ans

    else:
        i = 0
        while True:
            if a <= (b << i):
                ans = i
                break
            i += 1
        return ans


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    cnt = [0] * n
    for i in range(1, n):
        k = compute(nums[i - 1], nums[i]) + cnt[i-1]
        if k > 0:
            cnt[i] = k
    # print(cnt)
    ret = sum(cnt)
    print(ret)
