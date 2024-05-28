# -*- coding: utf-8 -*-
# @Time: 2024/4/2 14:25
# @Author: yfwang
# @File: 1950G.py
# bitmasks

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
    sangs = [input().split() for _ in range(n)]
    genres = dict()
    writers = dict()
    i1 = i2 = 0
    for genre, writer in sangs:
        if genre not in genres:
            genres[genre] = i1
            i1 += 1
        if writer not in writers:
            writers[writer] = i2
            i2 += 1
    nums1 = []
    nums2 = []
    for genre, writer in sangs:
        nums1.append(genres[genre])
        nums2.append(writers[writer])

    dp = [[0] * n for _ in range(1 << n)]
    for j in range(n):
        dp[1 << j][j] = 1
    for b in range(1, 1 << n):
        for i in range(n):
            if not (b & (1 << i)):
                continue
            for j in range(n):
                if b & (1 << j):
                    continue
                if nums1[i] != nums1[j] and nums2[i] != nums2[j]:
                    continue
                dp[b | 1 << j][j] = max(dp[b | 1 << j][j], dp[b][i] + 1)
    mx = 0
    for i in range(1 << n):
        mx = max(mx, max(dp[i]))
    print(n - mx)
