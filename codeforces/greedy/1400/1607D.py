# -*- coding: utf-8 -*-
# @Time: 2024/4/9 9:06
# @Author: yfwang
# @File: 1607D.py
# https://codeforces.com/problemset/problem/1607/D

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
    nums = LI()
    s = input()
    decreases = []
    increases = []
    for i, c in enumerate(s):
        if c == 'B':
            decreases.append(nums[i])
        else:
            increases.append(nums[i])
    decreases.sort(reverse=True)
    increases.sort(reverse=True)
    for p in range(1, n+1):
        if decreases and decreases[-1] >= p:
            decreases.pop()
        elif increases and increases[-1] <= p:
            increases.pop()
        else:
            YN(False)
            break
    else:
        YN(True)
