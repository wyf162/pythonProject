# -*- coding : utf-8 -*-
# @Time: 2023/10/6 13:30
# @Author: yefei.wang
# @File: 1006_three-colors.py

import sys

sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = [I() for _ in range(n)]
mod = 998244353

f = [0] * 90001
g = [0] * 90001
f[0] = g[0] = 3

for i in range(n):
    for j in range(90000, -1, -1):
        f[j] = (f[j] * 2 + f[max(j - a[i], 0)]) % mod
        if j >= a[i]:
            g[j] = (g[j] + g[j - a[i]]) % mod

s = sum(a)

if s % 2 == 0:
    dup = g[s // 2]
else:
    dup = 0
ans = pow(3, n, mod) - (f[(s + 1) // 2] - dup)
ans += mod
ans %= mod
print(ans)
