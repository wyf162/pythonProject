from collections import *
from itertools import *
from functools import *
from heapq import *
import sys, math

input = sys.stdin.readline


# https://judge.yosupo.jp/submission/96127
class SegmentTreeDual():

    def __init__(self, n, op, id, commutative=False):
        self.n = n
        self.op = op
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [id] * self.size
        self.lz = [id] * (2 * self.size)
        self.commutative = commutative

    def build(self, arr):
        for i, a in enumerate(arr):
            self.d[i] = a

    def propagate(self, k):
        if self.lz[k] == self.id: return
        if k < self.size:
            self.lz[2 * k] = self.op(self.lz[k], self.lz[2 * k], )
            self.lz[2 * k + 1] = self.op(self.lz[k], self.lz[2 * k + 1])
        else:
            self.d[k - self.size] = self.op(self.lz[k], self.d[k - self.size])
        self.lz[k] = self.id

    def get(self, p):
        res = self.d[p]
        p += self.size
        for i in range(self.log + 1):
            res = self.op(self.lz[p >> i], res)
        return res

    def range_apply(self, l, r, f):
        if l == r: return
        l += self.size
        r += self.size
        if not self.commutative:
            for i in range(1, self.log + 1)[::-1]:
                self.propagate(l >> i)
                self.propagate(r >> i)
        while l < r:
            if l & 1:
                self.lz[l] = self.op(f, self.lz[l])
                l += 1
            if r & 1:
                r -= 1
                self.lz[r] = self.op(f, self.lz[r])
            l >>= 1
            r >>= 1

    def all_propagate(self):
        for i in range(1, 2 * self.size):
            self.propagate(i)

    def all_apply(self, f):
        if not self.commutative:
            self.all_propagate()
        self.lz[1] = self.op(f, self.lz[1])

    def get_all(self):
        self.all_propagate()
        return self.d[:self.n]


MASK = (1 << 32) - 1
MOD = 998244353


def op(x, y):
    x1, x2 = x >> 32, x & MASK
    y1, y2 = y >> 32, y & MASK
    z1 = (x1 * y1) % MOD
    z2 = (x1 * y2 + x2) % MOD
    return (z1 << 32) + z2


N, M = map(int, input().split())
A = list(map(int, input().split()))
dst = SegmentTreeDual(N, op, 1 << 32, False)
dst.build(A)

for _ in range(M):
    l, r, x = map(int, input().split())
    l -= 1
    b = (r - l - 1) * pow(r - l, MOD - 2, MOD) % MOD
    c = x * pow(r - l, MOD - 2, MOD) % MOD
    dst.range_apply(l, r, (b << 32) + c)

res = []
for i in range(N):
    g = dst.get(i)
    b, c = g >> 32, g & MASK
    res.append((b + c) % MOD)
print(*res)
