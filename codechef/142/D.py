# -*- coding : utf-8 -*-
# @Time: 2024/7/10 23:20
# @Author: yefei.wang
# @File: D.py
# sortings FenwickTree

import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/FenwickTree.py
class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x


tcn = I()
for _tcn_ in range(tcn):
    n, x = MI()
    a = LI()
    indices = list(range(n))
    indices.sort(key=lambda x: a[x])
    pos = [0] * n
    for i in range(n):
        pos[indices[i]] = i

    b = [n - x for x in indices]
    F = FenwickTree(b)

    lo = 10 ** (x - 1)
    hi = 10 ** x
    ans = 0
    for i in range(n):
        F.update(pos[i], i - n)

        L = bisect.bisect_left(indices, lo - a[i], key=lambda x: a[x])
        R = bisect.bisect_left(indices, hi - a[i], key=lambda x: a[x])
        if L == R:
            continue
        ans += (i + 1) * (F.query(R) - F.query(L))
    print(ans)
