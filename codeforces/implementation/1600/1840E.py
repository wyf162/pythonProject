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

# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    s1 = list(input())
    s2 = list(input())
    ss = [s1, s2]
    t, q = MI()
    ops = [LGMI() for _ in range(q)]
    n = len(s1)
    diff = [0] * n
    cnt = 0
    for i in range(n):
        x = int(s1[i] != s2[i])
        diff[i] = x
        cnt += x

    ts = deque()
    for i in range(q):
        if ts and ts[0][0] + t <= i:
            _, pos = ts.popleft()
            if s1[pos] == s2[pos]:
                diff[pos] = 0
            else:
                diff[pos] = 1
            cnt += diff[pos]

        if ops[i][0] == 0:
            pos = ops[i][1]
            cnt -= diff[pos]
            ts.append((i, pos))
        elif ops[i][0] == 1:
            i1, pos1, i2, pos2 = ops[i][1:]
            ss[i1][pos1], ss[i2][pos2] = ss[i2][pos2], ss[i1][pos1]
            if s1[pos1] == s2[pos1]:
                cnt = cnt + 0 - diff[pos1]
                diff[pos1] = 0
            else:
                cnt = cnt + 1 - diff[pos1]
                diff[pos1] = 1

            if s1[pos2] == s2[pos2]:
                cnt = cnt + 0 - diff[pos2]
                diff[pos2] = 0
            else:
                cnt = cnt + 1 - diff[pos2]
                diff[pos2] = 1
        elif ops[i][0] == 2:
            if cnt == 0:
                print('Yes')
            else:
                print('No')
