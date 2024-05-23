# -*- coding : utf-8 -*-


class FenwickTree2:
    """
    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    https://github.com/atcoder/ac-library/blob/master/document_en/fenwicktree.md
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: int) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


class FenwickTree:
    def __init__(self, n, iter=None):
        self.n = n
        if iter is not None:
            self.bit = list(iter)

            for i in range(self.n):
                if i | (i + 1) < self.n:
                    self.bit[i | (i + 1)] += self.bit[i]
        else:
            self.bit = [0] * n
        length = (self.n + 1).bit_length() - 1
        self.powers = [1 << i for i in range(length, -1, -1)]
        self.tot = 0

    def sum(self, r):
        res = 0
        while r >= 0:
            res += self.bit[r]
            r = (r & (r + 1)) - 1
        return res

    def rsum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def add(self, idx, delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx = idx | (idx + 1)
        self.tot += delta

    def bisect_min_larger(self, num):
        if num <= 0: return -1
        note = -1
        tmp = 0
        for power in self.powers:
            if note + power >= self.n or \
                tmp + self.bit[note + power] >= num: continue
            note += power
            tmp += self.bit[note]
        return note + 1

    def bisect_max_smaller(self, num):
        if num > self.tot: return self.n
        note = -1
        tmp = 0
        for power in self.powers:
            if note + power >= self.n or \
                tmp + self.bit[note + power] >= num: continue
            note += power
            tmp += self.bit[note]
        return note

