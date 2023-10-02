# -*- coding : utf-8 -*-
# @Time: 2023/9/25 20:37
# @Author: yefei.wang
# @File: 1873H.py
import math
import os
import sys
from collections import Counter, deque
from io import BytesIO, IOBase

BUFSIZE = 8192
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')
sys.setrecursionlimit(10 ** 6)


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


# sys.stdin = open('./../input.txt', 'r')
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# mad city

tcn = I()
for _ in range(tcn):
    n, a, b = MI()
    edges = [LI() for i in range(n)]
    if a == b:
        print('NO')
        continue

    g = [[] for i in range(n + 1)]
    deg = [0 for i in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if deg[i] == 1:
            q.append(i)
    vis = [0 for i in range(n + 1)]
    k = 1
    while q:
        for i in range(len(q)):
            x = q.popleft()
            vis[x] = k
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1 and vis[y] == 0:
                    q.append(y)
        k += 1
    # if vis[b] == 0:
    #     print('YES')
    #     continue
    #
    # if 0 < vis[b] < vis[a]:
    #     print('YES')
    #     continue

    db = 0
    q = deque()
    q.append(b)
    find_ring = False
    bvis = [True for i in range(n+1)]
    bvis[b] = False
    while True:
        for i in range(len(q)):
            x = q.popleft()
            if vis[x] == 0:
                node = x
                find_ring = True
                break
            for y in g[x]:
                if bvis[y]:
                    q.append(y)
                    bvis[y] = False
        if find_ring:
            break
        db += 1

    dx = 0
    q = deque()
    q.append(a)
    find_ring = False
    bvis = [True for i in range(n+1)]
    bvis[a] = False
    while True:
        for i in range(len(q)):
            x = q.popleft()
            if x == node:
                find_ring = True
                break
            for y in g[x]:
                if bvis[y]:
                    q.append(y)
                    bvis[y] = False
        if find_ring:
            break
        dx += 1

    if db == 0 or db < dx:
        print('YES')
    else:
        print('NO')
