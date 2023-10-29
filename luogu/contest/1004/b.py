# -*- coding : utf-8 -*-
# @Time: 2023/10/4 14:44
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('./../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
mod = 911451407

ans = n * pow(2, n-1, mod)
ans %= mod
print(ans)
