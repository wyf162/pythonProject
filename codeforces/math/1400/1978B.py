# -*- coding : utf-8 -*-
# @Time: 2024/6/17 22:36
# @Author: yefei.wang
# @File: 1978B.py

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
    n, a, b = MI()
    mid = (2 * b - 2 * a + 1) // 2
    mid = max(mid, 0)
    mid = min(mid, n, b)
    ans = n * a
    for x in range(mid - 2, mid + 3):
        if x < 0 or x > n or x > b:
            continue
        ans = max(ans, x * (2 * b - x + 1) // 2 + (n - x) * a)
    print(ans)
