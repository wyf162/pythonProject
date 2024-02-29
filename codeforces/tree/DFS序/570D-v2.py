import bisect
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

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
N = 500005

n, m = MI()
tree = [[] for i in range(N)]
for y, x in enumerate(LI(), start=1):
    tree[x - 1].append(y)

s = input()

A = [0] * 26
for i in range(26):
    A[i] = (1 << i)

in_seq = [0] * N
out_seq = [0] * N
ts = 0
hh_ts = [[0] for _ in range(N)]
hh_xor = [[0] for _ in range(N)]

stk = [[0, 0, 0]]
while stk:
    x, h, flag = stk.pop()
    if flag == 0:
        ts += 1
        in_seq[x] = ts
        hh_ts[h].append(ts)
        hh_xor[h].append(hh_xor[h][-1] ^ A[ord(s[x]) - 97])
        stk.append([x, h + 1, 1])
        for y in tree[x]:
            stk.append([y, h + 1, 0])
    else:
        ts += 1
        out_seq[x] = ts

for i in range(m):
    v, h = MI()
    v -= 1
    h -= 1
    l = bisect.bisect_left(hh_ts[h], in_seq[v])
    r = bisect.bisect_left(hh_ts[h], out_seq[v])
    if l >= r:
        print('Yes')
        continue
    l = max(l - 1, 0)
    r -= 1
    t = hh_xor[h][l] ^ hh_xor[h][r]
    if t & (t - 1) == 0:
        print('Yes')
    else:
        print('No')
