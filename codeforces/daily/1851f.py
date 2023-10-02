# -*- coding : utf-8 -*-
# @Time: 2023/9/13 20:03
# @Author: yefei.wang
# @File: 1851f.py
import os
import sys
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


class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.idx = -1


class Trie:

    def __init__(self, h):
        self.h = h
        self.root = TrieNode()

    def insert(self, num, idx):
        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr] is None:
                node.children[lr] = TrieNode()
            node = node.children[lr]
        node.idx = idx

    def minimum_xor(self, num):
        mx = 0
        mask = 0

        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr]:
                node = node.children[lr]
                if lr == 0:
                    mask |= (1 << i)
                mx |= (1 << i)
            elif node.children[lr ^ 1]:
                node = node.children[lr ^ 1]
            else:
                print('break')
                break
        return mx, mask, node.idx


def solve(n, k, nums):
    trie = Trie(k)
    trie.insert(nums[0], 0)
    ans = 0
    l, r, x = 0, 1, 0
    for j, num in enumerate(nums[1:]):
        mx, mask, i = trie.minimum_xor(num)
        if mx > ans:
            ans = mx
            l, r, x = i, j + 1, mask
        trie.insert(num, j + 1)
    print(l + 1, r + 1, x)
    # print(f"max: {(nums[l] ^ x) & (nums[r] ^ x)}")


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        solve(n, k, nums)


if __name__ == '__main__':
    # sys.stdin = open('input.txt', 'r')
    main()
