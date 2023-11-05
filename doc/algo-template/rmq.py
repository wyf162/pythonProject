# -*- coding : utf-8 -*-
# @Time: 2023/10/29 14:39
# @Author: yefei.wang
# @File: rmq.py

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
