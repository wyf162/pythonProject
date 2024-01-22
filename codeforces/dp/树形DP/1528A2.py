# -*- coding : utf-8 -*-
# @Time: 2024/1/22 22:34
# @Author: yefei.wang
# @File: 1528A2.py

import os
import sys
from io import BytesIO, IOBase


# import time
# import functools
# import re
# from copy import deepcopy


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


BUFSIZE = 4096


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

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

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()


sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))


def GMI():
    return map(lambda x: int(x) - 1, input().split())


def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

t = II()
for _ in range(t):
    n = II()
    lefts = []
    rights = []
    for _ in range(n):
        l, r = MII()
        lefts.append(l)
        rights.append(r)

    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)

    parent = [-1] * n
    stack = [0]
    order = []
    while stack:
        u = stack.pop()
        for v in path[u]:
            if v and parent[v] == -1:
                parent[v] = u
                stack.append(v)
                order.append(v)

    res0 = [0] * n
    res1 = [0] * n
    order.reverse()
    for u in order:
        res0[parent[u]] += max(abs(lefts[parent[u]] - lefts[u]) + res0[u],
                               abs(lefts[parent[u]] - rights[u]) + res1[u])
        res1[parent[u]] += max(abs(rights[parent[u]] - lefts[u]) + res0[u],
                               abs(rights[parent[u]] - rights[u]) + res1[u])
    print(max(res0[0], res1[0]))
