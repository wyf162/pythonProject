# -*- coding: utf-8 -*-
# @Time: 2024/7/19 13:34
# @Author: yfwang
# @File: 190E.py
# 优化建图

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
nodes = []
last_idx = []
path = [-1] * n


def add_edge(u, v):
    last_idx.append(path[u])
    path[u] = len(nodes)
    nodes.append(v)


def neighbors(u):
    cur = path[u]
    while cur >= 0:
        yield nodes[cur]
        cur = last_idx[cur]


for _ in range(m):
    u, v = GMI()
    add_edge(u, v)
    add_edge(v, u)

ans = []
to_search = set(range(n))

while to_search:
    x = to_search.pop()
    stk = [x]
    cc = []
    while stk:
        x = stk.pop()
        cc.append(x)
        new_to_search = set()
        for y in neighbors(x):
            if y in to_search:
                to_search.remove(y)
                new_to_search.add(y)
        for x in to_search:
            stk.append(x)
        to_search = new_to_search
    ans.append([len(cc) - 1] + cc)

print(len(ans))
for i in range(len(ans)):
    print(' '.join(str(x + 1) for x in ans[i]))
