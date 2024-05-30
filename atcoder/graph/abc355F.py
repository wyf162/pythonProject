# -*- coding: utf-8 -*-
# @Time: 2024/5/30 15:09
# @Author: yfwang
# @File: abc355F.py
# https://atcoder.jp/contests/abc355/tasks/abc355_f
# dsu mst link-cut-tree

class Union_find():
    def __init__(self, N):  # N要素のUnion_find. A.Union_find(N)で作る.
        self.Group = [i for i in range(N)]
        self.Nodes = [1] * (N)

    def find(self, x):  # find(a)=find(b)のとき同じグループ
        while self.Group[x] != x:
            x = self.Group[x]
        return x

    def Union(self, x, y):
        if self.find(x) != self.find(y):
            if self.Nodes[self.find(x)] < self.Nodes[self.find(y)]:

                self.Nodes[self.find(y)] += self.Nodes[self.find(x)]
                self.Nodes[self.find(x)] = 0
                self.Group[self.find(x)] = self.find(y)

            else:
                self.Nodes[self.find(x)] += self.Nodes[self.find(y)]
                self.Nodes[self.find(y)] = 0
                self.Group[self.find(y)] = self.find(x)


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
inf = 10 ** 18

n, q = MI()

US = [Union_find(n) for i in range(10)]
DS = [n - 1] * 10

for i in range(n - 1):
    a, b, c = MI()
    a -= 1
    b -= 1
    for x in range(c - 1, 10):
        if US[x].find(a) != US[x].find(b):
            US[x].Union(a, b)
            DS[x] -= 1

for i in range(q):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    for x in range(c - 1, 10):
        if US[x].find(a) != US[x].find(b):
            US[x].Union(a, b)
            DS[x] -= 1

    ANS = sum(DS) + n - 1
    print(ANS)
