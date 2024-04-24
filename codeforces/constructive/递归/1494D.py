# -*- coding : utf-8 -*-
# @Time: 2024/4/24 22:00
# @Author: yefei.wang
# @File: 1494D.py
# https://codeforces.com/contest/1494/problem/D

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
A = [LI() for _ in range(n)]

ref = [-9] * n
sal = [-9] * n


def f(P, par=-1):
    if len(P) == 1:
        i = P.pop()
        ref[i] = par
        sal[i] = A[i][i]
        return
    i = P[0]
    mx = -1 << 32
    for j in P:
        if A[i][j] > mx:
            mx = A[i][j]
    Ps = []
    assigned = set()
    for k1 in P:
        if k1 in assigned:
            continue
        cur = []
        for k2 in P:
            if k2 not in assigned and A[k1][k2] < mx:
                assigned.add(k2)
                cur.append(k2)
        Ps.append(cur)
    idx = len(ref)
    ref.append(par)
    sal.append(mx)

    for W in Ps:
        f(W, idx)


f(P=list(range(n)))
sz = len(ref)
print(sz)
print(*sal)
print(n + 1)
for i in range(sz):
    if i == n:
        continue
    print(i + 1, ref[i] + 1)
