# -*- coding : utf-8 -*-
# @Time: 2023/10/25 20:09
# @Author: yefei.wang
# @File: 1076E.py

import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
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
            self.newlines = b.count(b"\n") + (not b)
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
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MI()
    u -= 1
    v -= 1
    g[v].append(u)
    g[u].append(v)

q = [[] for _ in range(n)]

m = I()
for _ in range(m):
    v, d, x = MI()
    q[v - 1].append([d, x])

add = [0] * n
res = [0] * n


@bootstrap
def dfs(v, pr, h, s):
    for d, x in q[v]:
        l, r = h, h + d
        add[l] += x
        if r + 1 < n:
            add[r + 1] -= x
    s += add[h]
    res[v] = s
    for u in g[v]:
        if u != pr:
            yield dfs(u, v, h + 1, s)
    for d, x in q[v]:
        l, r = h, h + d
        add[l] -= x
        if r + 1 < n:
            add[r + 1] += x
    yield


dfs(0, 0, 0, 0)

print(' '.join(map(str, res)))
