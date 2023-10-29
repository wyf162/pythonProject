# -*- coding : utf-8 -*-
# @Time: 2023/10/16 21:05
# @Author: yefei.wang
# @File: 1093D.py
import os
import sys
from io import BytesIO, IOBase

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

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

pow_2 = [1 for i in range(3 * 10 ** 5 + 1)]
for i in range(1, 3 * 10 ** 5 + 1):
    pow_2[i] = (pow_2[i - 1] * 2) % mod

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    # if m == 0:
    #     print(pow(3, n, mod))
    #     continue

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = MI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    tags = [-1 for i in range(n)]
    rst = 1
    q = []

    for i in range(n):
        if tags[i] != -1:
            continue
        q.append(i)
        tags[i] = 0
        c = [0, 0]
        while q:
            x = q.pop()
            c[tags[x]] += 1
            for y in g[x]:
                if tags[y] == -1:
                    tags[y] = tags[x] ^ 1
                    q.append(y)
                elif tags[y] ^ tags[x] ^ 1:
                    rst = 0
                    break
            if rst == 0: break
        if rst == 0: break
        rst *= pow_2[c[0]] + pow_2[c[1]]
        rst %= mod

    print(rst)
