# -*- coding : utf-8 -*-
# @Time: 2024/1/19 20:06
# @Author: yefei.wang
# @File: E.py

import bisect
import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, k = MI()
A = LI()
B = LI()
PA = [0] * (n + 1)
PB = [0] * (n + 1)
for i in range(n):
    PA[i + 1] = PA[i] + A[i]
    PB[i + 1] = PB[i] + B[i]


class RMQ:
    def __init__(self, init):
        self.N = len(init)
        self.LOGN = int(math.log2(self.N) + 1)
        self.f = [[0] * self.N for _ in range(self.LOGN)]
        for i in range(self.N):
            self.f[0][i] = init[i]
        for i in range(1, self.LOGN):
            for j in range(self.N - (1 << i) + 1):
                self.f[i][j] = min(self.f[i - 1][j], self.f[i - 1][j + (1 << (i - 1))])

    def query(self, l, r):
        k = int(math.log2(r - l))
        return min(self.f[k][l], self.f[k][r - (1 << k)])


rmq = RMQ(PB)

mx = sum(B)
for i in range(1, n + 1):
    if PA[i] < k:
        continue
    r = bisect.bisect_left(PA, PA[i] - k)
    v = rmq.query(0, r)
    mx = max(mx, PB[i] - v)
print(mx)
