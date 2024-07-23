# -*- coding : utf-8 -*-
# @Time: 2024/7/23 22:36
# @Author: yefei.wang
# @File: A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    nums = []
    for i in range(1, n):
        nums.append(i)
        nums.append(i)
    nums.append(n)
    c = 0
    while k > 0:
        k -= nums.pop()
        c += 1
    print(c)
