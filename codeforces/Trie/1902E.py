# -*- coding: utf-8 -*-
# @Time: 2024/7/23 13:13
# @Author: yfwang
# @File: 1902E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def f(s, t):
    if s == '':
        return len(t)
    if t == '':
        return len(s)
    if s[0] == t[-1]:
        return f(s[1:], t[:-1])
    else:
        return len(s) + len(t)


def solve():
    n = I()
    ss = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            x = f(ss[i], ss[j])
            ans += x
            # print(ss[i], ss[j], x)
    print(ans)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

    __slots__ = ['children', 'count']


# todo optimize Memory
# 换成 26*n 的数组
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for c in s:
            i = ord(c) - ord('a')
            if node.children[i]:
                node.children[i].count += 1
            else:
                node.children[i] = TrieNode()
                node.children[i].count += 1
            node = node.children[i]

    def query(self, s):
        node = self.root
        cnt = 0
        for c in s:
            i = ord(c) - ord('a')
            if node.children[i]:
                cnt += node.children[i].count
                node = node.children[i]
            else:
                break
        return cnt


def solve2():
    n = I()
    ss = [input() for _ in range(n)]
    trie = Trie()
    m = 0
    for s in ss:
        trie.insert(s)
        m += len(s)

    ans = m * n
    for s in ss:
        t = s[::-1]
        ans -= trie.query(t)

    print(ans * 2)


tcn = 1
for _tcn_ in range(tcn):
    solve2()
