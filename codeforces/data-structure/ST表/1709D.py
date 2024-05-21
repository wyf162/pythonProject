# -*- coding : utf-8 -*-
# @Time: 2024/5/21 21:44
# @Author: yefei.wang
# @File: 1709D.py

import sys
import math

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


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


n, m = MI()
nums = LI()
rmq = RMQ(nums)
q = I()
for i in range(q):
    x1, y1, x2, y2, k = MI()
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx % k or dy % k:
        print('NO')
        continue
    if y1 > y2: y1, y2 = y2, y1
    mx = rmq.query(y1 - 1, y2)
    can = 0
    if x1 > mx:
        can += 1
    else:
        c1 = (mx - x1 + k) // k
        if x1 + c1 * k <= n:
            can += 1
    if x2 > mx:
        can += 1
    else:
        c2 = (mx - x2 + k) // k
        if x2 + c2 * k <= n:
            can += 1
    if can == 2:
        print('YES')
    else:
        print('NO')
