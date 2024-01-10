# -*- coding : utf-8 -*-
# @Time: 2024/1/5 19:13
# @Author: yefei.wang
# @File: C.py

import sys

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

n = I()
A = LI()
right = 10 ** 9 + 1
for i in range(n):
    right = min(right, (A[i] + 1) / (i + 1))

print('%.10f' % right)
