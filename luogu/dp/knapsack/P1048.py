# -*- coding : utf-8 -*-
# @Time: 2023/10/2 16:48
# @Author: yefei.wang
# @File: P1048.py

import sys
sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

W, n = MI()
a = [LI() for _ in range(n)]
dp = [0] * (W+1)
for i in range(n):
    wi, vi = a[i]
    for w in range(W, wi-1, -1):
        dp[w] = max(dp[w], dp[w-wi] + vi)
print(dp[-1])
