# -*- coding : utf-8 -*-
# @Time: 2023/10/3 0:26
# @Author: yefei.wang
# @File: P1077.py


import sys
sys.stdin = open('./../../input.txt', 'r')

MOD = 10**6+7

input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
dp = [[0 for j in range(m+1)] for i in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(m+1):
        for k in range(min(j, a[i-1])+1):
            dp[i][j] += dp[i-1][j-k]

rst = dp[-1][-1]
rst %= MOD
print(rst)
