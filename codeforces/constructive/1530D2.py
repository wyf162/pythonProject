# -*- coding : utf-8 -*-
# @Time: 2024/1/22 21:03
# @Author: yefei.wang
# @File: 1520D2.py

import sys
from collections import deque

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = [0] + LI()
    b = [deque() for _ in range(n + 1)]
    for i in range(1, n + 1):
        b[a[i]].append(i)

    k, j = n, 1
    i = n
    while i > 0:
        if len(b[a[i]]) <= 1:
            i -= 1
            continue
        while j <= n and len(b[j]) >= 1:
            j += 1
        if b[a[i]][0] == j:
            x = b[a[i]].pop()
            a[x] = j
            b[j].append(x)
        else:
            x = b[a[i]].popleft()
            a[x] = j
            b[j].append(x)
        k -= 1
    print(k)
    print(*a[1:])
