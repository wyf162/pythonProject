# -*- coding : utf-8 -*-
# @Time: 2024/1/6 20:13
# @Author: yefei.wang
# @File: D.py

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

N = I()
mtx = [[None for _ in range(N)] for _ in range(N)]
mtx[N // 2][N // 2] = 'T'
mtx[0][0] = 1

v = 1
i, j = 0, 0
d = 'R'
for _ in range(N * N - 2):
    if d == 'R':
        if j + 1 < N and mtx[i][j + 1] is None:
            j += 1
            v += 1
            mtx[i][j] = v
        else:
            i += 1
            v += 1
            mtx[i][j] = v
            d = 'D'
    elif d == 'D':
        if i + 1 < N and mtx[i + 1][j] is None:
            i += 1
            v += 1
            mtx[i][j] = v
        else:
            j -= 1
            v += 1
            mtx[i][j] = v
            d = 'L'
    elif d == 'L':
        if j - 1 >= 0 and mtx[i][j - 1] is None:
            j -= 1
            v += 1
            mtx[i][j] = v
        else:
            i -= 1
            v += 1
            mtx[i][j] = v
            d = 'U'
    elif d == 'U':
        if i - 1 >= 0 and mtx[i - 1][j] is None:
            i -= 1
            v += 1
            mtx[i][j] = v
        else:
            j += 1
            v += 1
            mtx[i][j] = v
            d = 'R'

for r in range(N):
    print(*mtx[r])
