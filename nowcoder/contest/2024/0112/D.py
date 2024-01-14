# -*- coding : utf-8 -*-
# @Time: 2024/1/12 20:47
# @Author: yefei.wang
# @File: D.py


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

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    odd = sum(x & 1 for x in s)
    even = n - odd + 1
    res = odd * even
    if k == 0:
        print(res)
        continue

    x = y = 0
    for i in range(n + 1):
        x += s[i] & 1
        y += not (s[i] & 1)
        res = max(res, (y + odd - x) * (x + even - y))
    print(res)
