import os
import sys
from collections import deque, Counter
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
# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

n, m, k = MI()
a = LI()
edges = [LGMI() for _ in range(m)]
if k == 1:
    exit(print(min(a)))


def check(c):
    g = [[] for _ in range(n)]
    deg = [-1] * n
    for u, v in edges:
        if deg[u] < 0:
            deg[u] = 0
        if deg[v] < 0:
            deg[v] = 0
        if a[u] > c or a[v] > c:
            continue
        g[u].append(v)
        deg[v] += 1

    depth = Counter()
    q = deque(i for i, d in enumerate(deg) if d == 0)
    while q:
        x = q.popleft()
        for y in g[x]:
            depth[y] = max(depth[y], depth[x] + 1)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
    has_circle = any(d > 0 for d in deg)
    if has_circle:
        return True
    if depth and max(depth.values()) + 1 >= k:
        return True
    return False


sa = sorted(a)
l, r = 0, n - 1
ans = -1

while l <= r:
    mid = (l + r) // 2
    c = sa[mid]
    if check(c):
        ans = c
        r = mid - 1
    else:
        l = mid + 1

print(ans)
