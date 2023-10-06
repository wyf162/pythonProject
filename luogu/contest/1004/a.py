# -*- coding : utf-8 -*-
# @Time: 2023/10/4 14:36
# @Author: yefei.wang
# @File: a.py

import sys

sys.stdin = open('./../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

l, r, k = MI()

ans = 0
fac = [0] * (r + 1)
for x in range(1, r + 1):
    fac[x] = fac[x - 1] * x
    fac[x] %= k
    if x >= l:
        ans = max(ans, fac[x])
print(ans)
