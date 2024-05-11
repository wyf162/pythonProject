# -*- coding : utf-8 -*-
# @Time: 2024/5/11 10:34
# @Author: yefei.wang
# @File: 1028C.py


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

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    rects = [LI() for _ in range(n)]
    N = 10 ** 9 + 1
    prefix = [[-N, -N, N, N]]
    for i in range(n):
        x1, x2, x3, x4 = prefix[-1]
        y1, y2, y3, y4 = rects[i]
        z1, z2, z3, z4 = max(x1, y1), max(x2, y2), min(x3, y3), min(x4, y4)
        prefix.append([z1, z2, z3, z4])

    suffix = [[-N, -N, N, N]]
    for i in reversed(range(n)):
        x1, x2, x3, x4 = suffix[-1]
        y1, y2, y3, y4 = rects[i]
        z1, z2, z3, z4 = max(x1, y1), max(x2, y2), min(x3, y3), min(x4, y4)
        suffix.append([z1, z2, z3, z4])

    for i in range(n):
        x1, x2, x3, x4 = prefix[i]
        y1, y2, y3, y4 = suffix[n - 1 - i]
        z1, z2, z3, z4 = max(x1, y1), max(x2, y2), min(x3, y3), min(x4, y4)
        if z1 <= z3 and z2 <= z4:
            print(z1, z2)
            break
