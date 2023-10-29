# -*- coding : utf-8 -*-
# @Time: 2023/10/7 12:47
# @Author: yefei.wang
# @File: P2415.py

import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

a = LI()
n = len(a)
s = 0
for i in range(n):
    s += a[i] * (1 << (n-1))
print(s)