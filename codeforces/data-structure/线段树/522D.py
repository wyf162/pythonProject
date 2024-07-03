# -*- coding: utf-8 -*-
# @Time: 2024/7/3 10:32
# @Author: yfwang
# @File: 522D.py
# -*- coding: utf-8 -*-

import random
import sys
import typing


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
inf = 10 ** 9

tcn = 2
for _tcn_ in range(tcn):
    n, m = LI()
    rnd = random.getrandbits(20)
    A = [x ^ rnd for x in LI()]

    LS, RS = [], []
    for _ in range(m):
        L, R = GMI()
        LS.append(L)
        RS.append(R)
    pre = [-inf for _ in range(n)]
    nex = [inf for _ in range(n)]

    hst = dict()
    for i, a in enumerate(A):
        if a in hst:
            pre[i] = hst[a]
        hst[a] = i

    hst = dict()
    for i in range(n - 1, -1, -1):
        a = A[i]
        if a in hst:
            nex[i] = hst[a]
        hst[a] = i

    idxs = sorted(range(m), key=lambda x: LS[x])
    fmin = lambda x, y: x if x < y else y
    Lst = SegTree(fmin, inf, [i - pre[i] for i in range(n)])

    ans = [0] * m
    i1 = 0
    for i2 in idxs:
        while i1 < LS[i2]:
            if nex[i1] < n:
                Lst.set(nex[i1], inf)
            i1 += 1
        ans[i2] = Lst.prod(LS[i2], RS[i2] + 1)
    ans = [x if x < inf else -1 for x in ans]
    print('\n'.join(str(x) for x in ans))
