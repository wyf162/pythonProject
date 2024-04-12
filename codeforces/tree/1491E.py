# -*- coding: utf-8 -*-
# @Time: 2024/4/12 9:09
# @Author: yfwang
# @File: 1491E.py
# https://codeforces.com/problemset/problem/1491/E

import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007

n = I()
g = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

fib = [1, 1]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
# print(fib)
if fib[-1] != n:
    exit(print('NO'))

q = [(0, - 1)]
tree = [[] for _ in range(n)]
while q:
    v, p = q.pop()
    for u in g[v]:
        if u != p:
            tree[v].append(u)
            q.append((u, v))

q0 = [(0, len(fib) - 1)]
subtree = [0] * n
used = [False] * n

while q0:
    node, idx = q0.pop()
    if idx <= 3:
        continue
    f1, f2 = fib[idx - 1], fib[idx - 2]
    q = [node]
    path = []
    while q:
        v = q.pop()
        subtree[v] = 1
        for u in tree[v]:
            if used[u]:
                continue
            path.append((v, u))
            q.append(u)
    for v, u in reversed(path):
        if subtree[u] in [f1, f2]:
            break
        subtree[v] += subtree[u]
    else:
        exit(print('NO'))
    used[u] = True
    if subtree[u] == f1:
        q0.append((u, idx - 1))
        q0.append((node, idx - 2))
    else:
        q0.append((u, idx - 2))
        q0.append((node, idx - 1))
print('YES')
