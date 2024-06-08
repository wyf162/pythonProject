# -*- coding : utf-8 -*-
# @Time: 2024/6/8 13:01
# @Author: yefei.wang
# @File: D.py

import sys
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
# sys.stdout = open('../../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353


def count(c, mi, mx):
    if mi > c:
        return 0
    else:
        x1 = c - mi + 1
        x2 = max(c - mx + 1, 1)
        ret = (x1 + x2) * (x1 - x2 + 1) // 2
        return ret


n = I()
A = LI()
m = I()
queries = [LI() + [i] for i in range(m)]
queries.sort(key=lambda x: -x[0])

xi = [(i, a) for i, a in enumerate(A)]
xi.sort(key=lambda x: -x[1])
vis = [0] * n
dsu = DSU(n)

hst = dict()
pre_cc = []
j = 0
ans = [-1] * m

for i, a in xi:
    vis[i] = 1
    if i - 1 >= 0 and vis[i - 1] and not dsu.same(i-1,i):
        if dsu.leader(i - 1) in hst:
            del hst[dsu.leader(i - 1)]
        if dsu.leader(i) in hst:
            del hst[dsu.leader(i)]
        dsu.merge(i - 1, i)
    if i + 1 < n and vis[i + 1] and not dsu.same(i+1, i):
        if dsu.leader(i + 1) in hst:
            del hst[dsu.leader(i + 1)]
        if dsu.leader(i) in hst:
            del hst[dsu.leader(i)]
        dsu.merge(i + 1, i)
    hst[dsu.leader(i)] = dsu.size(i)

    while j < m and queries[j][0] > a:
        _, mi, mx, oi = queries[j]
        cnt = 0
        for c in pre_cc:
            cnt += count(c, mi, mx)
        ans[oi] = cnt
        j += 1
    pre_cc = list(hst.values())

for _, mi, mx, oi in queries:
    if ans[oi] == -1:
        ans[oi] = count(n, mi, mx)

print('\n'.join(str(x) for x in ans))
