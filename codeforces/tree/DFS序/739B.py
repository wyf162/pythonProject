# -*- coding: utf-8 -*-
# @Time: 2024/4/2 10:08
# @Author: yfwang
# @File: 739B.py

import sys
from bisect import bisect_left
from types import GeneratorType


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


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LI()

k = n.bit_length()
tree = [[] for _ in range(n)]
parent = [[-1] * n for _ in range(k)]
dist = [[0] * n for _ in range(k)]

for i in range(1, n):
    p, d = MI()
    p -= 1
    parent[0][i] = p
    tree[p].append(i)
    dist[0][i] = d

for i in range(k - 1):
    for j in range(n):
        if parent[i][j] != -1:
            parent[i + 1][j] = parent[i][parent[i][j]]
            dist[i + 1][j] = dist[i][j] + dist[i][parent[i][j]]

ans = [0] * n
for i in range(1, n):
    ans[parent[0][i]] += 1
    cur = nums[i]
    for j in range(k - 1, -1, -1):
        if parent[j][i] != -1 and dist[j][i] <= cur:
            cur -= dist[j][i]
            i = parent[j][i]
    if i: ans[parent[0][i]] -= 1

stack = [0]
order = []
while stack:
    u = stack.pop()
    order.append(u)
    for v in tree[u]:
        stack.append(v)

for u in reversed(order):
    if u:
        ans[parent[0][u]] += ans[u]

print(' '.join(map(str, ans)))
