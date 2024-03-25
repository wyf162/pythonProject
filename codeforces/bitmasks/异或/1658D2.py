# -*- coding: utf-8 -*-
# @Time: 2024/3/25 17:02
# @Author: yfwang
# @File: 1658D2.py

class TrieNode:
    def __init__(self):
        self.children = [None] * 2


class Trie:

    def __init__(self, h):
        self.h = h
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr] is None:
                node.children[lr] = TrieNode()
            node = node.children[lr]

    def maximum_xor(self, num):
        mx = 0

        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr ^ 1]:
                node = node.children[lr ^ 1]
                mx |= (1 << i)
            elif node.children[lr]:
                node = node.children[lr]
            else:
                break
        return mx


import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    l, r = MI()
    nums = LI()
    if (r - l + 1) % 2:
        tx = 0
        for x in range(l, r + 1):
            tx ^= x
        for x in nums:
            tx ^= x
        print(tx)
        # print(*[tx ^ a for a in nums])
        continue

    trie = Trie(17)

    xor = 0
    for x in range(l, r):
        xor ^= x

    n = len(nums)
    tot = 0
    for i in range(n):
        tot ^= nums[i]
        trie.insert(nums[i])

    for i in range(n):
        v = tot ^ nums[i]
        tx = xor ^ v
        if tx ^ nums[i] == r and trie.maximum_xor(tx) <= r:
            print(tx)
            # print(*[tx ^ a for a in nums])
            break
