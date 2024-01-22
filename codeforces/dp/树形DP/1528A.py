# -*- coding : utf-8 -*-
# @Time: 2024/1/22 21:55
# @Author: yefei.wang
# @File: 1528A.py

import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType

BUFSIZE = 8192


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
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    L, R = [], []
    for _ in range(n):
        x, y = MI()
        L.append(x)
        R.append(y)
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    dpl = [0] * n
    dpr = [0] * n

    @bootstrap
    def dfs(x, fa, LorR):
        ret = 0
        v = L[x] if LorR == 0 else R[x]
        for y in g[x]:
            if y == fa:
                continue
            yield dfs(y, x, 0)
            yield dfs(y, x, 1)
            ret += max(abs(v - L[y]) + dpl[y], abs(v - R[y]) + dpr[y])
        if LorR == 0:
            dpl[x] = ret
        else:
            dpr[x] = ret
        yield

    dfs(0, -1, 0)
    dfs(0, -1, 1)

    ans = max(dpl[0], dpr[0])
    print(ans)
