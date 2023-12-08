# -*- coding : utf-8 -*-
# @Time: 2023/10/4 0:23
# @Author: yefei.wang
# @File: P3379-lca-Q1.py

import sys
from functools import lru_cache
import os
import sys
from io import BytesIO, IOBase

sys.stdin = open('./../input.txt', 'r')

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

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

B = 21

n, qs, root = MI()
edges = [LI() for _ in range(n - 1)]
queries = [LI() for _ in range(qs)]

g = [[] for i in range(n + 1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

depth = [0] * (n + 1)
father = [[0] * B for i in range(n + 1)]


def dfs(x, fa, dep):
    depth[x] = dep
    father[x][0] = fa
    for y in g[x]:
        if y != fa:
            dfs(y, x, dep + 1)


dfs(root, 0, 1)

for i in range(1, B):
    for x in range(1, n + 1):
        father[x][i] = father[father[x][i - 1]][i - 1]


@lru_cache(None)
def lca(x, y):
    # 令depth[y] > depth[x]
    if depth[x] > depth[y]:
        x, y = y, x
    tmp = depth[y] - depth[x]
    for j in range(B):
        if tmp >> j & 1:
            y = father[y][j]
    if y == x:
        return x

    for j in range(B - 1, -1, -1):
        px, py = father[x][j], father[y][j]
        if px != py:
            x, y = px, py
    return father[x][0]


for a, b in queries:
    c = lca(a, b)
    print(c)
