# -*- coding: utf-8 -*-
# @Time: 2024/4/22 13:10
# @Author: yfwang
# @File: demo.py

n = 4
f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
g = [[0 for _ in range(n + 2)] for _ in range(n + 2)]


def modify(x1, y1, x2, y2):
    # 左闭右闭
    f[x1][y1] += 1
    f[x2 + 1][y2 + 1] += 1
    f[x1][y2 + 1] -= 1
    f[x2 + 1][y1] -= 1


def acc():
    for i in range(n):
        for j in range(n):
            g[i + 1][j + 1] = f[i][j] + g[i + 1][j] + g[i][j + 1] - g[i][j]


def pp():
    for i in range(1, n + 1):
        print(*g[i][1:-1])


if __name__ == '__main__':
    # modify(0, 0, 1, 3)
    modify(2, 0, 3, 3)
    acc()
    pp()
