# -*- coding: utf-8 -*-
# @Time: 2024/5/22 13:17
# @Author: yfwang
# @File: 1716C.py

import math


class RMQ:
    def __init__(self, init):
        self.N = len(init)
        self.LOGN = int(math.log2(self.N) + 1)
        self.f = [[0] * self.N for _ in range(self.LOGN)]
        for i in range(self.N):
            self.f[0][i] = init[i]
        for i in range(1, self.LOGN):
            for j in range(self.N - (1 << i) + 1):
                self.f[i][j] = max(self.f[i - 1][j], self.f[i - 1][j + (1 << (i - 1))])

    def query(self, l, r):
        k = int(math.log2(r - l))
        return max(self.f[k][l], self.f[k][r - (1 << k)])


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
inf = 10 ** 18

tcn = I()
for _tcn_ in range(tcn):
    m = I()
    mtx = [LI() for _ in range(2)]
    nums1 = mtx[0] + mtx[1][::-1]
    for i in range(2 * m):
        nums1[i] += 2 * m - i

    nums2 = mtx[1] + mtx[0][::-1]
    for i in range(2 * m):
        nums2[i] += 2 * m - i

    rmq1 = RMQ(nums1)
    rmq2 = RMQ(nums2)

    ans = inf
    cur = 0
    i, j = 0, 0
    for _ in range(m - 1):
        # reminder = mtx[i][j + 1:] + mtx[i ^ 1][j:][::-1]
        if i == 0:
            k = 2 * m - j * 2 - 1
            mx = rmq1.query(j + 1, j + 1 + k )
            tmp = max(cur + k, mx - (2 * m - j - 1 - k))
        else:
            k = 2 * m - j * 2 - 1
            mx = rmq2.query(j + 1, j + 1 + k)
            tmp = max(cur + k, mx - (2 * m - j - 1 - k))

        # print(k == len(reminder))
        # tmp1 = max(x + len(reminder) - i for i, x in enumerate(reminder))
        # tmp1 = max(cur + len(reminder), tmp1)
        # print(tmp, tmp1)
        ans = min(ans, tmp)
        cur = max(cur + 2, mtx[i ^ 1][j] + 2, mtx[i ^ 1][j + 1] + 1)
        i ^= 1
        j += 1
    tmp = max(cur + 1, mtx[i ^ 1][j] + 1)
    ans = min(ans, tmp)
    print(ans)
