# -*- coding : utf-8 -*-
# @Time: 2024/1/6 20:02
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = I()
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if i + j + k <= N:
                print(i, j, k)
