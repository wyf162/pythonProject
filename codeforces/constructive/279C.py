# -*- coding : utf-8 -*-
# @Time: 2023/10/16 23:40
# @Author: yefei.wang
# @File: 279C.py
import sys
# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


n, m = MI()
a = LI()
queries = [LI() for _ in range(m)]

f = [n]*n
f[n-1] = n-1
for i in range(n-2, -1, -1):
    if a[i] <= a[i+1]:
        f[i] = f[i+1]
    else:
        f[i] = i
# print(f)

g = [-1]*n
g[0] = 0
for i in range(1, n, 1):
    if a[i-1] >= a[i]:
        g[i] = g[i-1]
    else:
        g[i] = i
# print(g)
for query in queries:
    l, r = query
    l -= 1
    r -= 1
    if f[l] >= g[r]:
        print('Yes')
    else:
        print('No')

