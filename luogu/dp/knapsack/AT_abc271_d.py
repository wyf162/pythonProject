# -*- coding : utf-8 -*-
# @Time: 2023/10/2 16:58
# @Author: yefei.wang
# @File: AT_abc271_d.py

import sys
sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, W = MI()
a = [LI() for _ in range(n)]
dp = [[False for j in range(W+1)] for i in range(n+1)]
dp[0][0] = True

for i in range(n):
    wt, wh = a[i]
    for w in range(W, -1, -1):
        if w-wt >= 0:
            dp[i+1][w] |= dp[i][w-wt]
        if w-wh >= 0:
            dp[i+1][w] |= dp[i][w-wh]

if not dp[n][W]:
    print('No')
    exit(0)

ret = ''
w = W
for i in range(n-1, -1, -1):
    wt, wh = a[i]
    if dp[i][w-wt]:
        ret = 'H' + ret
        w -= wt
    else:
        ret = 'T' + ret
        w -= wh

print('Yes')
print(ret)

# s = 0
# for i, th in enumerate(ret):
#     if th == 'T':
#         s += a[i][0]
#     else:
#         s += a[i][1]
# print(s)
