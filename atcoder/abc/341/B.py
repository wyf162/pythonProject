# -*- coding : utf-8 -*-
# @Time: 2024/2/17 19:59
# @Author: yefei.wang
# @File: B.py

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdin = open('./../../input.txt', 'r')
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
st = [LI() for _ in range(n-1)]

for i in range(n-1):
    A[i+1] += A[i] // st[i][0] * st[i][1]
print(A[-1])


