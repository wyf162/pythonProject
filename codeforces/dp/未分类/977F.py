# -*- coding : utf-8 -*-
# @Time: 2023/10/10 20:59
# @Author: yefei.wang
# @File: 977F.py

import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()

hst = Counter()
dp = [1] * n
mx, mv = 0, 0
for i in range(n):
    dp[i] = hst[a[i]-1] + 1
    hst[a[i]] = max(hst[a[i]], dp[i])
    if dp[i] > mx:
        mx = dp[i]
        mv = a[i]
print(mx)
s = mv - mx + 1
for i in range(n):
    if a[i] == s:
        print(i+1, end=' ')
        s += 1
print()
