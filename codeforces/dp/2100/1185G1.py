# -*- coding: utf-8 -*-
# @Time: 2024/7/19 9:19
# @Author: yfwang
# @File: 1185G1.py

import sys
import math

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

N = 16
f = [[[[0, 0, 0] for _ in range(N)] for _ in range(N)] for _ in range(N)]
f[1][0][0][0] = f[0][1][0][1] = f[0][0][1][2] = 1

for a in range(1, N * 3 - 3):
    for i in range(min(a + 1, N)):
        for j in range(min(a - i + 1, N)):
            k = a - i - j
            if i + 1 >= N or j + 1 >= N or k + 1 >= N:
                continue
            f[i + 1][j][k][0] += f[i][j][k][1] + f[i][j][k][2]
            f[i][j + 1][k][1] += f[i][j][k][0] + f[i][j][k][2]
            f[i][j][k + 1][2] += f[i][j][k][0] + f[i][j][k][1]

tcn = 1
for _tcn_ in range(tcn):
    n, T = MI()
    times = []
    genres = []
    for _ in range(n):
        time, genre = MI()
        times.append(time)
        genres.append(genre - 1)

    ans = 0
    for x in range(1 << n):
        tot = 0
        cnt = [0 for _ in range(3)]
        for i in range(n):
            if x >> i & 1:
                tot += times[i]
                cnt[genres[i]] += 1
        c0, c1, c2 = cnt
        if tot == T and max(c0, c1, c2) * 2 - 1 <= c0 + c1 + c2:
            ans += sum(f[c0][c1][c2]) * math.factorial(c0) * math.factorial(c1) * math.factorial(c2)
            ans %= mod
    print(ans)
