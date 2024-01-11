import os
import sys
from collections import deque
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

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n, k, c = MI()
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


    # v1, v2 是树直径的两个端点。
    mx1, v1 = bfs(0)
    mx2, v2 = bfs(v1)


    def bfs2(start):
        dist = [0] * n
        q = deque([(start, -1)])
        step = -1
        while q:
            step += 1
            for _ in range(len(q)):
                x, fa = q.popleft()
                dist[x] = step
                for y in g[x]:
                    if y != fa:
                        q.append((y, x))
        return dist


    dist1 = bfs2(0)
    dist2 = bfs2(v1)
    dist3 = bfs2(v2)

    rst = mx1 * k
    for x in range(1, n):
        d1 = dist1[x]
        d2 = dist2[x]
        d3 = dist3[x]
        md = max(d2, d3)
        rst = max(rst, md * k - d1 * c)
    print(rst)
