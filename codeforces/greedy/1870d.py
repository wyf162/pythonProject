import heapq
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 4096
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')


# sys.stdin = open('../input.txt', 'r')
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
I = lambda: input()
II = lambda: int(input())
MI = lambda: map(str, input().split())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
ZLI = lambda: [0] + list(map(int, input().split()))


def solve(n, c, k):
    hst = dict()
    cvi = [(v, -i) for i, v in enumerate(c, start=1)]
    heapq.heapify(cvi)
    mi, i = heapq.heappop(cvi)
    hst[-i] = k // mi
    k = k % mi

    pre = mi
    pre_i = i
    while cvi and k:
        mi, i = heapq.heappop(cvi)
        diff = mi - pre
        if diff == 0 or i > pre_i:
            continue
        elif k >= diff:
            mk = min(hst[-pre_i], k // diff)
            hst[-pre_i] -= mk
            hst[-i] = mk
            k -= mk * diff
            pre, pre_i = mi, i
        else:
            break
    mx = max(hst.keys())
    diff = [0] * max(mx + 2, n + 1)
    for k, v in hst.items():
        diff[0] += v
        diff[k] -= v
    ans = [0] * n
    ans[0] = diff[0]
    for i in range(1, n):
        ans[i] = ans[i - 1] + diff[i]
    print(' '.join(map(str, ans)))


def main():
    tcn = II()
    for _ in range(tcn):
        n = II()
        c = LII()
        k = II()
        solve(n, c, k)


if __name__ == '__main__':
    main()