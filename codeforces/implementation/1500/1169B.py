import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 4096
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')


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
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
edges = [LI() for _ in range(m)]
# edges.sort()

# select a1, b1, a2, b2

a1, b1 = edges[0]
a2, b2 = -1, -1


# a2, b2 = edges[-1]


for i in range(m):
    if edges[i][0] not in [a1, b1] and edges[i][1] not in [a1, b1]:
        a2, b2 = edges[i]
        break

if a2 < 0:
    exit(print('YES'))


def check(x, y):
    for i in range(m):
        if edges[i][0] in [x, y] or edges[i][1] in [x, y]:
            continue
        else:
            return False
    return True


for x, y in [(a1, a2), (a1, b2), (b1, a2), (b1, b2)]:
    if check(x, y):
        exit(print('YES'))
print('NO')
