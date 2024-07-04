# -*- coding: utf-8 -*-
# @Time: 2024/7/4 10:34
# @Author: yfwang
# @File: 455C.py

import os
import sys
from collections import deque
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

# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
TGMI = lambda: tuple(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m, q = MI()
g = [[] for _ in range(n)]
N = n
fa = [_ for _ in range(N)]
dh = [-1 for _ in range(N)]


def find(x):
    r = x
    while r != fa[r]:
        r = fa[r]

    k = x
    while k != r:
        fa[k], k = r, fa[k]
    return fa[x]


def union(x, y):
    fx, fy = find(x), find(y)
    dh[fy] = max(dh[fx], dh[fy], (dh[fx] + 1) // 2 + (dh[fy] + 1) // 2 + 1)
    fa[fx] = fy


for i in range(m):
    u, v = GMI()
    union(u, v)
    g[u].append(v)
    g[v].append(u)


def bfs(start: int, dist: list) -> int:
    dist[start] = res = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] != -1:
                continue
            dist[v] = dist[u] + 1
            res = max(res, dist[v])
            q.append(v)
    return u


dist0 = [-1] * n
dist1 = [-1] * n
for i in range(n):
    if find(i) == i:
        L = bfs(i, dist0)
        R = bfs(L, dist1)
        dh[i] = dist1[R]

for _ in range(q):
    op = LGMI()
    if op[0] == 0:
        x = op[1]
        print(dh[find(x)])
    elif op[0] == 1:
        x, y = op[1], op[2]
        if find(x) == find(y):
            continue
        else:
            union(x, y)
