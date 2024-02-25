# -*- coding : utf-8 -*-
# @Time: 2024/2/24 13:21
# @Author: yefei.wang
# @File: 1898C.py

# https://codeforces.com/problemset/problem/1898/C

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
    n, m, k = MI()
    if k < n + m - 2 or (k - (n + m - 2)) % 2 == 1:
        print('NO')
        continue
    mtx1 = [['R' for _ in range(m - 1)] for _ in range(n)]
    mtx2 = [['B' for _ in range(m)] for _ in range(n - 1)]

    for i in range(m - 1):
        if i % 2 == 1:
            mtx1[0][i] = 'B'
    # if (m-1) % 2:
    #     cur = 'R'
    # else:
    #     cur = 'B'
    for i in range(n - 1):
        if (m - 1) % 2:
            if i % 2 == 0:
                mtx2[i][-1] = 'B'
            else:
                mtx2[i][-1] = 'R'
        else:
            if i % 2 == 0:
                mtx2[i][-1] = 'R'
            else:
                mtx2[i][-1] = 'B'
    if mtx2[-1][-1] == 'B':
        mtx2[-1][-2] = 'R'
        mtx1[-2][-1] = 'B'
        mtx1[-1][-1] = 'B'

    print('YES')
    for i in range(n):
        print(*mtx1[i])
    for i in range(n - 1):
        print(*mtx2[i])
