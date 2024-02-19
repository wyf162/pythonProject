# -*- coding : utf-8 -*-
# @Time: 2024/2/9 15:00
# @Author: yefei.wang
# @File: 1338B.py


import sys

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
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

dist = [-1] * n
dist[0] = 0
stk = [0]
while stk:
    u = stk.pop()
    for v in g[u]:
        if dist[v] == -1:
            dist[v] = dist[u] ^ 1
            stk.append(v)

val = -1
ans1 = 1

cnt1 = 0
cnt2 = 0
for i in range(n):
    if len(g[i]) == 1:
        if val == -1:
            val = dist[i]
        elif val != dist[i]:
            ans1 = 3
        cnt1 += 1
    else:
        for j in g[i]:
            if len(g[j]) == 1:
                cnt2 += 1
                break
ans2 = n - 1 - cnt1 + cnt2
print(ans1, ans2)
