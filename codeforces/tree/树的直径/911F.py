# -*- coding: utf-8 -*-
# @Time: 2024/4/19 9:43
# @Author: yfwang
# @File: 911F.py
# https://codeforces.com/problemset/problem/911/F

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
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)


def bfs(start):
    q = deque([(start, -1)])
    step = -1
    while q:
        step += 1
        for _ in range(len(q)):
            x, fa = q.popleft()
            for y in g[x]:
                if y != fa:
                    q.append((y, x))
    return step, x


# 直径D, 两个端点是v1, v2
_, v1 = bfs(0)
D, v2 = bfs(v1)

depth = [-1] * n
fa = [-1] * n
dfs = []
stk = [0]
fa[0] = n
depth[0] = 1

while stk:
    x = stk.pop()
    dfs.append(x)
    for y in g[x]:
        if fa[y] == -1:
            fa[y] = x
            depth[y] = depth[x] + 1
            stk.append(y)
fa[0] = -1

B = 30
father = [[0] * B for i in range(n)]
for x in range(n):
    father[x][0] = fa[x]

for i in range(1, B):
    for x in range(n):
        father[x][i] = father[father[x][i - 1]][i - 1]


def get_path(x, y):
    xx, yy = x, y
    # 令depth[y] > depth[x]
    if depth[x] > depth[y]:
        x, y = y, x
    tmp = depth[y] - depth[x]
    for j in range(B):
        if tmp >> j & 1:
            y = father[y][j]
    if y == x:
        if depth[y] < depth[x]:
            lca = x
        else:
            lca = y
        path1 = [xx]
        while path1[-1] != lca:
            path1.append(fa[path1[-1]])
        path2 = [yy]
        while path2[-1] != lca:
            path2.append(fa[path2[-1]])
        path = path1[:-1] + path2[::-1]
        return path

    for j in range(B - 1, -1, -1):
        px, py = father[x][j], father[y][j]
        if px != py:
            x, y = px, py
    lca = father[x][0]

    path1 = [xx]
    while path1[-1] != lca:
        path1.append(fa[path1[-1]])
    path2 = [yy]
    while path2[-1] != lca:
        path2.append(fa[path2[-1]])
    path = path1[:-1] + path2[::-1]
    return path


def get_dist(x, y):
    xx, yy = x, y
    # 令depth[y] > depth[x]
    if depth[x] > depth[y]:
        x, y = y, x
    tmp = depth[y] - depth[x]
    for j in range(B):
        if tmp >> j & 1:
            y = father[y][j]
    if y == x:
        return abs(depth[xx] - depth[yy])

    for j in range(B - 1, -1, -1):
        px, py = father[x][j], father[y][j]
        if px != py:
            x, y = px, py
    lca = father[x][0]
    return depth[xx] + depth[yy] - 2 * depth[lca]


# print(D, v1, v2)
diameter = get_path(v1, v2)
st = set(diameter)

deg = [0] * n
for i in range(n):
    deg[i] = len(g[i])

q = deque()
for i, d in enumerate(deg):
    if i in st:
        continue
    if deg[i] == 1:
        q.append(i)

tot = 0
ops = []
while q:
    x = q.pop()
    if x in st:
        continue
    d1 = get_dist(v1, x)
    d2 = get_dist(v2, x)
    if d1 > d2:
        ops.append((v1, x, x))
        tot += d1
    else:
        ops.append((v2, x, x))
        tot += d2
    for y in g[x]:
        deg[y] -= 1
        if deg[y] == 1 and y not in st:
            q.append(y)

for i in range(len(diameter) - 1, 0, -1):
    ops.append((v1, diameter[i], diameter[i]))
    tot += i
print(tot)
for i in range(n - 1):
    print(' '.join(str(x + 1) for x in ops[i]))
