# -*- coding: utf-8 -*-
# @Time: 2024/6/6 17:36
# @Author: yfwang
# @File: 827A.py

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

n = I()
S = []
A = []

N = 2 * 10 ** 6 + 5
fa = [_ for _ in range(N)]
ans = ['' for _ in range(N)]


def find(x):
    r = x
    while r != fa[r]:
        r = fa[r]

    k = x
    while k != r:
        fa[k], k = r, fa[k]
    return fa[x]


def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx > fy:
        fa[fy] = fx
    else:
        fa[fx] = fy


for i in range(n):
    s = input().split()
    S.append(s[0])
    A.append([int(x) - 1 for x in s[2:]])

for i in range(n):
    t = S[i]
    for pos in A[i]:
        j = find(pos)
        while j < pos + len(t):
            ans[j] = t[j - pos]
            union(j + 1, j)
            j = find(j)

while not ans[-1]:
    ans.pop()
for i in range(len(ans)):
    if not ans[i]:
        ans[i] = 'a'

ret = ''.join(ans)
print(ret)
