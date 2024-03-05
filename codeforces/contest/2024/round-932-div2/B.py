# -*- coding : utf-8 -*-
# @Time: 2024/3/5 22:44
# @Author: yefei.wang
# @File: B.py

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
    n = I()
    A = LI()
    mi = [n] * n
    mx = [-1] * n
    for i, a in enumerate(A):
        if a >= n:
            continue
        mi[a] = min(mi[a], i)
        mx[a] = max(mx[a], i)
    left = 0
    right = n
    ans = True
    for i in range(n):
        if mi[i] == n and mx[i] == -1:
            break
        if mi[i] == mx[i]:
            ans = False
            break

        left = max(left, mi[i])
        right = min(right, mx[i] - 1)
        if left > right:
            ans = False
            break
    if ans is False:
        print(-1)
    else:
        print(2)
        print(1, left + 1)
        print(left + 2, n)
