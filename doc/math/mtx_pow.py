# -*- coding: utf-8 -*-
# @Time: 2024/6/20 10:41
# @Author: yfwang
# @File: mtx_pow.py

def matrix_mul(A, B, mod=10 ** 9 + 7):
    n, m = len(A), len(A[0])
    p = len(B[0])
    ans = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= mod
    return ans


def matrix_pow(x, n):
    if n == 1: return x
    if n == 2: return matrix_mul(x, x)
    v = matrix_pow(x, n // 2)
    ans = matrix_mul(v, v)
    if n % 2 == 0:
        return ans
    return matrix_mul(ans, x)