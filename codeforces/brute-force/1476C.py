# -*- coding : utf-8 -*-
# @Time: 2024/1/27 13:31
# @Author: yefei.wang
# @File: 1476C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = float('inf')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    c = LI()
    a = LI()
    b = LI()
    cur = -inf
    ans = 0
    for i in range(1, n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        if a[i] == b[i]:
            cur = 2
            ans = max(ans, c[i] + 1)
        else:
            cur = max(b[i] - a[i] + 2, cur + c[i-1] - b[i] + a[i] + 1)
            ans = max(ans, c[i] - 1 + cur)
    print(ans)
