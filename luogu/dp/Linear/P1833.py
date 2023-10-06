# -*- coding : utf-8 -*-
# @Time: 2023/10/3 19:42
# @Author: yefei.wang
# @File: P1833.py

import sys

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

ts, te, n = input().split()
ts = int(ts.split(':')[0]) * 60 + int(ts.split(':')[1])
te = int(te.split(':')[0]) * 60 + int(te.split(':')[1])
n = int(n)
t = te - ts

nums = [LI() for _ in range(n)]
f = [0] * (t + 1)

for i in range(n):
    ti, ci, pi = nums[i]
    if pi == 0:
        for k in range(ti, t + 1, 1):
            f[k] = max(f[k], f[k - ti] + ci)
    else:
        c, b = 1, pi
        while b > 0:
            z = min(c, b)
            for k in range(t, ti * z - 1, -1):
                f[k] = max(f[k], f[k - ti * z] + ci * z)
            b -= c
            c *= 2

mx = max(f)
print(mx)
