# -*- coding : utf-8 -*-
# @Time: 2024/3/9 20:13
# @Author: yefei.wang
# @File: D.py


import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

t = input()
n = I()
ss = []
for _ in range(n):
    s = input().split()
    s.pop(0)
    ss.append(s)

m = len(t)
dp = [101] * (m + 1)
dp[0] = 0
for i in range(n):
    ndp = [101] * (m + 1)
    for j in range(m):
        for s in ss[i]:
            if dp[j] != 101 and t[j:].startswith(s):
                ndp[j + len(s)] = min(ndp[j + len(s)], dp[j] + 1)
    for j in range(m+1):
        ndp[j] = min(ndp[j], dp[j])
    dp = ndp

if dp[-1] == 101:
    print(-1)
else:
    print(dp[-1])
