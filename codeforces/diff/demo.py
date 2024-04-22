# -*- coding: utf-8 -*-
# @Time: 2024/4/22 13:10
# @Author: yfwang
# @File: demo.py

n = 4
diff = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
pre_sum = [[0 for _ in range(n + 2)] for _ in range(n + 2)]


def modify(x1, y1, x2, y2):
    # 左闭右闭
    diff[x1][y1] += 1
    diff[x2 + 1][y2 + 1] += 1
    diff[x1][y2 + 1] -= 1
    diff[x2 + 1][y1] -= 1


def acc():
    for i in range(n):
        for j in range(n):
            pre_sum[i + 1][j + 1] = diff[i][j] + pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j]


def pp():
    for i in range(1, n + 1):
        print(*pre_sum[i][1:-1])


if __name__ == '__main__':
    # modify(0, 0, 1, 3)
    modify(2, 0, 3, 3)
    acc()
    pp()
