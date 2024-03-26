# -*- coding: utf-8 -*-
# @Time: 2024/3/26 13:42
# @Author: yfwang
# @File: 1792D.py
# https://codeforces.com/problemset/problem/1792/D
# permutations

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


class Tree:
    def __init__(self):
        self.tree = {}

    def insert(self, tmp):
        note = self
        for val in tmp:
            if val not in note.tree:
                note.tree[val] = Tree()
            note = note.tree[val]

    def search(self, tmp):
        note = self
        for i in range(len(tmp)):
            if tmp[i] not in note.tree: return i
            note = note.tree[tmp[i]]
        return len(tmp)


tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    perms = [LGMI() for _ in range(n)]
    tree = Tree()
    for perm in perms:
        ind = [0] * m
        for i, v in enumerate(perm):
            ind[v] = i
        tree.insert(ind)

    ans = []
    for perm in perms:
        ans.append(tree.search(perm))
    print(*ans)
