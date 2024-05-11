# -*- coding : utf-8 -*-
# @Time: 2024/5/11 13:11
# @Author: yefei.wang
# @File: 1598C.py

import sys
from collections import Counter

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
    n = I()
    A = LI()
    tot = sum(A)
    if tot * 2 % n:
        print(0)
        continue
    mean = tot * 2 // n
    ans = 0
    hst = Counter()
    for a in A:
        ans += hst[mean-a]
        hst[a] += 1
    print(ans)
