# -*- coding: utf-8 -*-
# @Time: 2024/5/13 9:24
# @Author: yfwang
# @File: 799C.py


class LazySegmentTree:
    """
    Reference
    https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
    https://github.com/atcoder/ac-library/blob/master/document_en/lazysegtree.md
    https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    https://leetcode.cn/circle/discuss/4rJDBt/

    """

    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * self.size

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        self.all_apply(2 * k, self.lz[k])
        self.all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.id

    def build(self, v):
        assert len(v) <= self.n
        for i in range(len(v)):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, l, r, f):
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if (l >> i) << i != l:
                self.update(l >> i)
            if (r >> i) << i != r:
                self.update((r - 1) >> i)

    def max_right(self, l, g):
        assert 0 <= l <= self.n
        # assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                return 0


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
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n, c, d = MI()
    fountains = []
    for i in range(n):
        beauty, cost, typ = input().split()
        beauty, cost = int(beauty), int(cost)
        fountains.append((beauty, cost, typ))
    coins = []
    diamonds = []

    for i in range(n):
        beauty, cost, typ = fountains[i]
        if typ == 'C':
            coins.append((beauty, cost, i))
        elif typ == 'D':
            diamonds.append((beauty, cost, i))

    coins.sort(key=lambda x: x[1])
    diamonds.sort(key=lambda x: x[1])
    n1, n2 = len(coins), len(diamonds)
    Lstc = LazySegmentTree(n1, max, 0, max, max, 0)
    Lstd = LazySegmentTree(n2, max, 0, max, max, 0)
    hst = dict()
    for i in range(n1):
        Lstc.set(i, coins[i][0])
        hst[coins[i][2]] = i
    for i in range(n2):
        Lstd.set(i, diamonds[i][0])
        hst[diamonds[i][2]] = i

    def get_max_beauty(nums, money, typ):
        L, R = 0, len(nums) - 1
        ret = -1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid][1] <= money:
                ret = mid
                L = mid + 1
            else:
                R = mid - 1
        if ret >= 0:
            if typ == 'C':
                ret = Lstc.prod(0, ret + 1)
            elif typ == 'D':
                ret = Lstd.prod(0, ret + 1)
            return ret
        else:
            return 0


    ans = 0
    for i in range(n):
        c1, d1 = c, d
        beauty, cost, typ = fountains[i]
        tmp = 0
        if typ == 'C':
            if c1 >= cost:
                c1 = c - cost
                tmp = beauty
                Lstc.set(hst[i], 0)
        elif typ == 'D':
            if d1 >= cost:
                d1 = d - cost
                tmp = beauty
                Lstd.set(hst[i], 0)
        mx1 = get_max_beauty(coins, c1, 'C')
        mx2 = get_max_beauty(diamonds, d1, 'D')
        if typ == 'C':
            if c >= cost:
                Lstc.set(hst[i], beauty)
        elif typ == 'D':
            if d >= cost:
                Lstd.set(hst[i], beauty)

        if tmp == 0 or max(mx1, mx2) == 0:
            continue
        ans = max(ans, tmp + max(mx1, mx2))
    print(ans)
