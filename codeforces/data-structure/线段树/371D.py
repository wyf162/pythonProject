# -*- coding: utf-8 -*-
# @Time: 2024/4/18 9:07
# @Author: yfwang
# @File: 371D.py
# https://codeforces.com/problemset/problem/371/D

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
from functools import partial
from operator import lt, gt

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


def solve_brute_force():
    n = I()
    nums = LI()
    q = I()
    queries = [LI() for _ in range(q)]

    used = [0] * n
    for query in queries:
        if query[0] == 1:
            p, x = query[1] - 1, query[2]
            while x and p < n:
                if x <= nums[p] - used[p]:
                    used[p] += x
                    x = 0
                else:
                    x -= nums[p] - used[p]
                    used[p] = nums[p]
                p += 1
        elif query[0] == 2:
            p = query[1] - 1
            print(used[p])


n = I()
nums = LI()
q = I()
queries = [LI() for _ in range(q)]

# 合并左右区间的值
op = lambda a, b: a + b
# 线段树维护的值的幺元
e = 0
# 父结点的懒标记更新子结点的值
mapping = lambda f, x: 0 if f == 0 else x
# 父结点的懒标记更新子结点的懒标记(合并)
composition = lambda f, g: 0 if f == 0 else g
# 懒标记的幺元函数
id_ = 1

Lst = LazySegmentTree(n, op, e, mapping, composition, id_)

for i in range(n):
    Lst.set(i, nums[i])

# for i in range(n):
#     print(Lst.prod(i, i + 1), end=' ')
# print()

for query in queries:
    if query[0] == 1:
        p, x = query[1] - 1, query[2]
        i = Lst.max_right(p, partial(gt, x))
        if i < n:
            y = Lst.get(i) - (x - Lst.prod(p, i))
            # if y > Lst.get(i):
            #     for i in range(n):
            #         print(Lst.prod(i, i + 1), end=' ')
            #     print()
            #
            #     print(Lst.get(i), y)
            Lst.set(i, y)
        Lst.apply(p, i, 0)

    elif query[0] == 2:
        p = query[1] - 1
        ret = nums[p] - Lst.get(p)
        print(ret)
        # for i in range(n):
        #     print(Lst.prod(i, i + 1), end=' ')
        # print()
