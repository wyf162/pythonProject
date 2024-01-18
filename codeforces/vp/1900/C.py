import os
import sys
from collections import deque
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

# sys.stdin = open('./../../input.txt', 'r')
# sys.stdout = open('./../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = '#' + input()
    tree = [[]] + [LI() for _ in range(n)]
    fa = [0] * (n + 1)
    deg = [0] * (n + 1)
    for i in range(1, n + 1):
        left, right = tree[i]
        if left:
            fa[left] = i
            deg[i] += 1
        if right:
            fa[right] = i
            deg[i] += 1
    dp = [n] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if deg[i] == 0:
            q.append(i)
            dp[i] = 0

    while q:
        x = q.popleft()
        f = fa[x]
        if f == 0:
            continue
        # print(f)
        if tree[f][0] == x and s[f] == 'L':
            dp[f] = min(dp[f], dp[x])
        elif tree[f][1] == x and s[f] == 'R':
            dp[f] = min(dp[f], dp[x])
        else:
            dp[f] = min(dp[f], dp[x] + 1)
        deg[f] -= 1
        if deg[f] == 0:
            q.append(f)
    print(dp[1])
