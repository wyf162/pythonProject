import math
import os
import sys
from collections import Counter
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


# money trees

tcn = I()
for _ in range(tcn):
    n, k = MI()
    a = LI()
    h = LI()

    ans = 0 if min(a) > k else 1
    left = 0
    s = a[0]
    for right in range(1, n):
        if h[right - 1] % h[right] == 0:
            s += a[right]
            while s > k:
                s -= a[left]
                left += 1
            ans = max(right - left + 1, ans)

        else:
            left = right
            s = a[left]
            while s > k:
                s -= a[left]
                left += 1
            ans = max(right - left + 1, ans)
    print(ans)
