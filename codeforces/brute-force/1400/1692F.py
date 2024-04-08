# -*- coding: utf-8 -*-
# @Time: 2024/4/8 9:09
# @Author: yfwang
# @File: 1692F.py
# https://codeforces.com/problemset/problem/1692/F


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
    cnt = [0] * 10
    for x in nums:
        x %= 10
        cnt[x] += 1

    ans = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                v = i + j + k
                v %= 10
                if v == 3:
                    cnt[i] -= 1
                    cnt[j] -= 1
                    cnt[k] -= 1
                    if cnt[i] >= 0 and cnt[j] >= 0 and cnt[k] >= 0:
                        ans = True
                    cnt[i] += 1
                    cnt[j] += 1
                    cnt[k] += 1
    YN(ans)
