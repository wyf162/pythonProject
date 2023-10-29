# -*- coding : utf-8 -*-
# @Time: 2023/10/14 19:22
# @Author: yefei.wang
# @File: d.py
import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, q = MI()
qs = LI()
ks = [LI() for _ in range(m)]

f = [0] * (n + 1)
for i in range(n + 1):
    f[i] = max(f[i], f[i - 1])
    for j in range(m):
        k, s = ks[j]
        ni = i + (1 << k)
        if ni <= n:
            f[ni] = max(f[ni], f[i] + s)

pre = 0
ans = 0
for i in range(q):
    diff = qs[i] - pre - 1
    ans += f[diff]
    pre = qs[i]

diff = n - pre
ans += f[diff]
print(ans)
