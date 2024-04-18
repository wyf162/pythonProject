# -*- coding: utf-8 -*-
# @Time: 2024/4/18 13:25
# @Author: yfwang
# @File: 1010D.py
# https://codeforces.com/problemset/problem/1010/D

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

import sys

n = int(input())
g = {
    'A': lambda a, b: v[a] & v[b],
    'O': lambda a, b: v[a] | v[b],
    'X': lambda a, b: v[a] ^ v[b],
    'N': lambda a: v[a] ^ 1,
    'I': lambda a: a + 1
}


def f(q):
    q = q.split()
    return q.pop(0)[0], [int(t) - 1 for t in q]


d = [f(q) for q in sys.stdin.readlines()]
t = [0]
for i in t:
    f, a = d[i]
    if f != 'I': t.extend(a)
v = [0] * n
for i in t[::-1]:
    f, a = d[i]
    v[i] = g[f](*a)
s = [0] * n
s[0] = 1
for i in t:
    if not s[i]: continue
    f, a = d[i]
    if f == 'I': continue
    for k in a:
        v[k] ^= 1
        s[k] = g[f](*a) != v[i]
        v[k] ^= 1
print(''.join(str(q ^ v[0]) for q, (f, a) in zip(s, d) if f == 'I'))
