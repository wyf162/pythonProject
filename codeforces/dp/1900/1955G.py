# -*- coding : utf-8 -*-
# @Time: 2024/6/29 8:16
# @Author: yefei.wang
# @File: 1955G.py
# gcd

import sys
from math import gcd

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
    n, m = MI()
    MAP = [LI() for _ in range(n)]
    DP = [[[] for i in range(m)] for j in range(n)]

    DP[0][0] = [MAP[0][0]]

    for i in range(n):
        for j in range(m):
            LIST = []
            if i - 1 >= 0:
                for x in DP[i - 1][j]:
                    LIST.append(gcd(x, MAP[i][j]))

            if j - 1 >= 0:
                for x in DP[i][j - 1]:
                    LIST.append(gcd(x, MAP[i][j]))

            LIST.sort()
            LIST2 = []
            for x in LIST:
                if LIST2 and LIST2[-1] == x:
                    continue
                LIST2.append(x)

            LIST = LIST2

            for ix in range(len(LIST)):
                for jx in range(ix + 1, len(LIST)):
                    if LIST[jx] % LIST[ix] == 0:
                        break
                else:
                    DP[i][j].append(LIST[ix])

    print(max(DP[-1][-1]))
