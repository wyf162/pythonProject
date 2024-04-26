# -*- coding: utf-8 -*-
# @Time: 2024/4/26 9:15
# @Author: yfwang
# @File: 1401F.py
# https://codeforces.com/problemset/problem/1401/F
# zkw

from sys import stdin

input = lambda: stdin.readline()[:-1]

n, q = map(int, input().split())
N = 1 << n
node = [0] * 2 * N
a = list(map(int, input().split()))
for i in range(N):
    node[N + i] = a[i]

for i in range(N - 1, 0, -1):
    node[i] = node[2 * i] + node[2 * i + 1]

X = 0
mask = N - 1


def swap(k):
    global X
    X ^= 1 << k


def reverse(k):
    global X
    for i in range(k):
        X ^= 1 << i


def update(x, k):
    node[x + N] = k
    res = N + x
    for i in range(1, n + 1):
        res >>= 1
        node[res] = node[2 * res] + node[2 * res + 1]


def query_sum(L, R):
    ans = 0
    for i in range(n + 1):
        if (L >> i) & 1 and L + (1 << i) <= R:
            ans += node[(L ^ X + N) >> i]
            L += 1 << i

    for i in range(n, -1, -1):
        if L + (1 << i) <= R:
            ans += node[(L ^ X + N) >> i]
            L += 1 << i

    return ans


for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, k = query[1:]
        update((x - 1) ^ X, k)
    if query[0] == 2:
        k = query[1]
        reverse(k)
    if query[0] == 3:
        k = query[1]
        swap(k)
    if query[0] == 4:
        l, r = query[1:]
        print(query_sum(l - 1, r))
