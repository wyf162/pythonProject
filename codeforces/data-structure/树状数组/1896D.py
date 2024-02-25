# -*- coding : utf-8 -*-
# @Time: 2024/2/25 19:18
# @Author: yefei.wang
# @File: 1896D.py
# https://codeforces.com/problemset/problem/1896/D

import typing


class FenwickTree:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, q = MI()
    nums = LI()
    fwt = FenwickTree(n)
    h1, h2 = [], []
    for i, num in enumerate(nums):
        fwt.add(i, num)
        if num == 1:
            heappush(h1, i)
            heappush(h2, -i)

    ops = [LI() for i in range(q)]
    for op in ops:
        if op[0] == 1:
            v = op[1]
            tot = fwt.sum(0, n)
            ans = False
            if v > tot:
                YN(ans)
                continue
            if (tot - v) % 2 == 0:
                ans = True
                YN(ans)
            else:
                while h1 and nums[h1[0]] != 1:
                    heappop(h1)
                if h1:
                    mx = fwt.sum(h1[0], n)
                    if v < mx:
                        ans = True
                while h2 and nums[-h2[0]] != 1:
                    heappop(h2)
                if h2:
                    mx = fwt.sum(0, -h2[0] + 1)
                    if v < mx:
                        ans = True
                YN(ans)
        else:
            _, i, x = op
            i -= 1
            fwt.add(i, x - nums[i])
            nums[i] = x
            if x == 1:
                heappush(h1, i)
                heappush(h2, -i)
