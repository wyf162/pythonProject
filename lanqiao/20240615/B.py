# -*- coding : utf-8 -*-
# @Time: 2024/6/15 19:26
# @Author: yefei.wang
# @File: B.py

import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

n, q = MI()
A = LI()
cnt = [0] * (n + 1)
for a in A:
    cnt[a] += 1

f = [0] * (n + 1)
pre = 0
cur = 1
for i in range(n + 1):
    f[i] = cur * pow(2, n - pre - cnt[i], mod)
    f[i] %= mod
    cur = cur * (pow(2, cnt[i], mod) - 1)
    cur %= mod
    pre += cnt[i]

queries = [I() for _ in range(q)]
for x in queries:
    ret = f[x]
    if x == 0:
        ret -= 1
    print(ret)
