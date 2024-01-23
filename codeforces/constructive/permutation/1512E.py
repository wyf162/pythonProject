# -*- coding : utf-8 -*-
# @Time: 2024/1/23 22:12
# @Author: yefei.wang
# @File: 1512E.py

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
    n, l, r, s = MI()
    d = r - l + 1
    mi = (1 + d) * d // 2
    mx = (n + n - d + 1) * d // 2
    if s < mi or s > mx:
        print(-1)
        continue
    x = n
    ans = [0] * n
    vis = set()
    for i in range(d):
        d1 = d - i - 1
        mi = (1 + d1) * d1 // 2
        while s - x < mi:
            x -= 1
        vis.add(x)
        ans[l+i-1] = x
        s -= x
        x -= 1
    curr = 1
    for i in range(l-1):
        while curr in vis:
            curr += 1
        ans[i] = curr
        curr += 1
    for i in range(r, n):
        while curr in vis:
            curr += 1
        ans[i] = curr
        curr += 1
    print(*ans)
