# -*- coding : utf-8 -*-
# @Time: 2024/3/6 22:41
# @Author: yefei.wang
# @File: D.py


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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    W = LI()
    W.sort(reverse=True)
    ans = 0
    for i, w in enumerate(W, start=1):
        ans = max(ans, i * w)
    print(ans)
