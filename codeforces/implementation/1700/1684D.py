# -*- coding : utf-8 -*-
# @Time: 2024/6/4 22:32
# @Author: yefei.wang
# @File: 1684D.py
# sortings

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    A = LI()
    tot = 0
    for i in range(n):
        tot += A[i]
        A[i] += i + 1
    A.sort(reverse=True)
    for i in range(k):
        tot -= A[i]
    for i in range(k):
        tot += n
        tot -= i
    print(tot)
