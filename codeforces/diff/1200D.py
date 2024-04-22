# -*- coding: utf-8 -*-
# @Time: 2024/4/22 15:24
# @Author: yfwang
# @File: 1200D3.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    mtx = [[int(c == 'W') for c in input()] for _ in range(n)]

    right = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    down = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n - 1, -1, -1):
            right[i][j] = right[i][j + 1] + mtx[i][j]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            down[i][j] = down[i + 1][j] + mtx[i][j]

    f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    g = [[0 for _ in range(n + 2)] for _ in range(n + 2)]


    def modify(x1, y1, x2, y2):
        # 左闭右闭
        f[x1][y1] += 1
        f[x2 + 1][y2 + 1] += 1
        f[x1][y2 + 1] -= 1
        f[x2 + 1][y1] -= 1


    for i in range(n):
        acc = 0
        for j in range(n):
            if acc == j and right[i][min(n, j + k)] >= n - j - k:
                x1 = max(0, i - k + 1)
                modify(x1, j, i, j)
            acc += mtx[i][j]

    for j in range(n):
        acc = 0
        for i in range(n):
            if acc == i and down[min(n, i + k)][j] >= n - i - k:
                y1 = max(0, j - k + 1)
                modify(i, y1, i, j)
            acc += mtx[i][j]

    for i in range(n):
        if right[i][0] == n:
            if i + 1 <= n - 1:
                modify(i + 1, 0, n - 1, n - 1)
            if i - k >= 0:
                modify(0, 0, i - k, n - 1)

    for j in range(n):
        if down[0][j] == n:
            if j + 1 <= n - 1:
                modify(0, j + 1, n - 1, n - 1)
            if j - k >= 0:
                modify(0, 0, n - 1, j - k)

    for i in range(n):
        for j in range(n):
            g[i + 1][j + 1] = f[i][j] + g[i + 1][j] + g[i][j + 1] - g[i][j]

    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, max(g[i][1:-1]))
    print(ans)
