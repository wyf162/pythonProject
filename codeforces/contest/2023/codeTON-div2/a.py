# -*- coding : utf-8 -*-
# @Time: 2023/9/18 22:34
# @Author: yefei.wang
# @File: a.py
# import sys

# sys.stdin = open('input.txt', 'r')
import os
import sys
from io import BytesIO, IOBase
from types import GeneratorType

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


# 使用快速输入输出，防止卡时间
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def solve(n, k, x):
    if k > n or k - 1 > x:
        print(-1)
        return
    s = k * (k - 1) // 2
    if k == x:
        x -= 1
    s += (n - k) * x
    print(s)
    return


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k, x = map(int, input().split())
        solve(n, k, x)


if __name__ == '__main__':
    main()
