# -*- coding : utf-8 -*-
# @Time: 2024/5/11 15:03
# @Author: yefei.wang
# @File: 1606D.py
# https://codeforces.com/contest/1606/problem/D
# sortings

from sys import stdin

input = lambda: stdin.readline()[:-1]


def solve():
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a + [i])
    mat.sort(key=lambda x: x[0])
    mxl = [[-1] * m for i in range(n)]
    mnl = [[1 << 20] * m for i in range(n)]
    mxr = [[-1] * m for i in range(n)]
    mnr = [[1 << 20] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            mxl[i][j] = mat[i][j]
            if i > 0:
                mxl[i][j] = max(mxl[i][j], mxl[i - 1][j])
            if j > 0:
                mxl[i][j] = max(mxl[i][j], mxl[i][j - 1])

    for i in range(n - 1, -1, -1):
        for j in range(m):
            mnl[i][j] = mat[i][j]
            if i < n - 1:
                mnl[i][j] = min(mnl[i][j], mnl[i + 1][j])
            if j > 0:
                mnl[i][j] = min(mnl[i][j], mnl[i][j - 1])

    for i in range(n):
        for j in range(m - 1, -1, -1):
            mnr[i][j] = mat[i][j]
            if i > 0:
                mnr[i][j] = min(mnr[i][j], mnr[i - 1][j])
            if j < m - 1:
                mnr[i][j] = min(mnr[i][j], mnr[i][j + 1])

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mxr[i][j] = mat[i][j]
            if i < n - 1:
                mxr[i][j] = max(mxr[i][j], mxr[i + 1][j])
            if j < m - 1:
                mxr[i][j] = max(mxr[i][j], mxr[i][j + 1])

    for i in range(n - 1):
        for j in range(m - 1):
            if mxl[i][j] < mnl[i + 1][j] and mxr[i + 1][j + 1] < mnr[i][j + 1]:
                print('YES')
                ans = ['R'] * n
                for k in range(i + 1):
                    ans[mat[k][-1]] = 'B'
                print(''.join(ans), j + 1)
                return
    print('NO')


for _ in range(int(input())):
    solve()
