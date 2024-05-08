# -*- coding : utf-8 -*-
# @Time: 2024/1/28 17:23
# @Author: yefei.wang
# @File: 1475E.py
import math
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

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    a.sort(reverse=True)
    c1 = c2 = 0
    i = k - 1
    while i >= 0:
        if a[i] == a[k-1]:
            c1 += 1
            i -= 1
        else:
            break
    i = k
    while i < n:
        if a[i] == a[k - 1]:
            c2 += 1
            i += 1
        else:
            break
    ans = math.comb(c1+c2, c1)
    ans %= mod
    print(ans)
