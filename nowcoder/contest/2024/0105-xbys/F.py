# -*- coding : utf-8 -*-
# @Time: 2024/1/5 23:26
# @Author: yefei.wang
# @File: F.py

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, l, r = MI()
a = LI()
dp = Counter()
dp[0] = 0
for i in range(n):
    ndp = Counter()
    for j in dp:
        if a[i] - j < l:
            ndp[min(j, a[i])] = max(ndp[min(j, a[i])], dp[j])
        elif a[i] - j > r:
            ndp[j] = max(ndp[j], dp[j])
            ndp[a[i] - r] = max(ndp[a[i] - r], dp[j] + 1)
        else:
            ndp[j] = max(ndp[j], dp[j] + 1)
    dp = ndp
ans = 0
for i in dp:
    ans = max(ans, dp[i])
print(ans)
