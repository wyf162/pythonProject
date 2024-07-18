# -*- coding : utf-8 -*-
# @Time: 2024/7/17 23:51
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = [(10 ** 9 + 1, 0, 0)]
    for i in range(n):
        l, r = MI()
        a.append((l, r, i))
    a.sort()
    ans, comp, mx = [0] * n, [], -1
    for l, r, i in a:
        if l >= mx:
            for u in comp:
                ans[u] = len(comp)
            comp = []
        comp.append(i)
        mx = max(mx, r)
    print(*ans)
