import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 4096


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

n, m = MII()
parent = [-1] + LGMI()
tree = [[] for _ in range(n)]
for i, v in enumerate(parent):
    if i: tree[v].append(i)

depth = [0] * n
stack = [0]
while stack:
    u = stack.pop()
    for v in tree[u]:
        depth[v] = depth[u] + 1
        stack.append(v)

s = I()
queries = [[] for _ in range(n)]
for idx in range(m):
    v, d = GMI()
    queries[v].append([d, idx])

ans = [0] * m
depth_xor_acc = [0] * n
stack = [[0, 0]]
while stack:
    u, flag = stack.pop()
    if not flag:
        for d, idx in queries[u]:
            ans[idx] ^= depth_xor_acc[d]
        depth_xor_acc[depth[u]] ^= 1 << (ord(s[u]) - ord('a'))
        stack.append([u, 1])
        for v in tree[u]:
            stack.append(([v, 0]))
    else:
        for d, idx in queries[u]:
            ans[idx] ^= depth_xor_acc[d]

for v in ans:
    print('Yes' if v & (v - 1) == 0 else 'No')
