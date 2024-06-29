# -*- coding : utf-8 -*-
# @Time: 2024/6/29 12:32
# @Author: yefei.wang
# @File: nd21d.py


X, Y, Z = 2, 3, 4


def idx(i, j, k):
    return i * Y * Z + (j * Z + k)


nums = [[[idx(i, j, k) for k in range(Z)] for j in range(Y)] for i in range(2)]

for i in range(X):
    for j in range(Y):
        for k in range(Z):
            print(nums[i][j][k])
