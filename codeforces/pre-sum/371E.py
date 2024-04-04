# -*- coding : utf-8 -*-
# @Time: 2024/4/4 9:57
# @Author: yefei.wang
# @File: 371E.py
# https://codeforces.com/problemset/problem/371/E

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

n = I()
nums = LI()
xi = [(x, i+1) for i, x in enumerate(nums)]
xi.sort()
k = I()
pre_sum = [0] * (n+1)
for i in range(n):
    pre_sum[i+1] = pre_sum[i] + xi[i][0]

tot = 0
for i in range(1, k):
    tot += xi[i][0] * i - pre_sum[i]

mi = tot
idx = 0
for i in range(k, n):
    tot += xi[i][0] * (k-1) - (pre_sum[i] - pre_sum[i-k+1])
    tot -= (pre_sum[i] - pre_sum[i-k+1]) - xi[i-k][0] * (k-1)
    if tot < mi:
        mi = tot
        idx = i - k + 1

ans = []
for i in range(k):
    ans.append(xi[idx+i][1])
print(*ans)

