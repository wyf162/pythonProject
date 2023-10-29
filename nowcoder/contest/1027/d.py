# -*- coding : utf-8 -*-
# @Time: 2023/10/28 10:17
# @Author: yefei.wang
# @File: d.py

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


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
c = [0] * m
for x in a:
    c[x - 1] += 1

s = [0] * (n + 2)
d = [0] * (n + 2)

for i in range(m):
    s[0] += c[i]
    d[1] += -1
    d[c[i] + 1] += 1

for i in range(1, n + 1):
    d[i] += d[i - 1]
    s[i] = s[i - 1] + d[i]

ans = [0] * m
for i in range(m):
    if n - c[i] < k:
        ans[i] = -1
        continue
    l, r = -1, n
    while l + 1 < r:
        mid = (l + r) // 2
        tot = s[mid]
        if tot - (c[i] - min(mid, c[i])) <= k:
            r = mid
        else:
            l = mid
    ans[i] = r

print(' '.join(map(str, ans)))
