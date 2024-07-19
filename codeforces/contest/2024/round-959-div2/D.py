# -*- coding : utf-8 -*-
# @Time: 2024/7/18 23:23
# @Author: yefei.wang
# @File: D.py
# Pigeonhole Principle

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    print('YES')
    used = [0] * n
    res = []
    for k in range(n - 1, 0, -1):
        box = [-1] * k
        for i in range(n):
            if used[i]:
                continue
            m = A[i] % k
            if box[m] == -1:
                box[m] = i
            else:
                j = box[m]
                res.append([i + 1, j + 1])
                used[j] = 1
                break
    res.reverse()
    for row in res:
        print(*row)
