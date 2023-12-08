# -*- coding : utf-8 -*-
# @Time: 2023/12/3 17:49
# @Author: yefei.wang
# @File: E.py

import sys


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.v = [0] * n

    @staticmethod
    def lowbit(i):
        return i & (-i)

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.v[i]
            i -= self.lowbit(i)
        return ans

    def update(self, i, x):
        while i < self.n:
            self.v[i] += x
            i += self.lowbit(i)


sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, q = MI()
a = LI()
c = [[] for i in range(n)]
stk = []
for i in range(n):
    while stk and a[stk[-1]] > a[i]:
        c[i].append(stk.pop())
    stk.append(i)

group = [[] for _ in range(n)]
for i in range(q):
    l, r = GMI()
    group[r].append([l, i])

fw = FenwickTree(n + 1)
ans = [0] * q
for i in range(n):
    for d in c[i]:
        fw.update(d + 1, 1)
    for l, j in group[i]:
        ans[j] = fw.query(i+1) - fw.query(l)
print(*ans)
