# -*- coding : utf-8 -*-
# @Time: 2023/10/30 21:05
# @Author: yefei.wang
# @File: P1253.py
import sys
from functools import lru_cache
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')
# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
a = [0] + LI()
N = 10 ** 6 + 5
tree = [0] * (N * 4)


def pushup(p):
    tree[p] = max(tree[p * 2], tree[p * 2 + 1])


def build(s, e, p):
    if s == e:
        tree[p] = a[s]
        return
    m = s + (e - s >> 1)
    build(s, m, p * 2)
    build(m + 1, e, p * 2 + 1)
    pushup(p)


def update1(l, r, c, s, e, p):
    if s == e:
        tree[p] = c
        return
    m = s + (e - s >> 1)
    if l <= m:
        update1(l, r, c, s, m, p * 2)
    if r > m:
        update1(l, r, c, m + 1, e, p * 2 + 1)
    pushup(p)


def update2(l, r, c, s, e, p):
    if s == e:
        tree[p] += c
        return
    m = s + (e - s >> 1)
    if l <= m:
        update2(l, r, c, s, m, p * 2)
    if r > m:
        update2(l, r, c, m + 1, e, p * 2 + 1)
    pushup(p)


def query(l, r, s, e, p):
    if l <= s and e <= r:
        return tree[p]
    m = s + (e - s >> 1)
    ret = float('-inf')
    if l <= m:
        ret = max(ret, query(l, r, s, m, p * 2))
    if r > m:
        ret = max(ret, query(l, r, m + 1, e, p * 2 + 1))
    return ret


build(1, n, 1)
for _ in range(q):
    op = LI()
    if op[0] == 1:
        l, r, c = op[1:]
        update1(l, r, c, 1, n, 1)
    elif op[0] == 2:
        l, r, c = op[1:]
        update2(l, r, c, 1, n, 1)
    elif op[0] == 3:
        l, r = op[1:]
        rst = query(l, r, 1, n, 1)
        print(rst)
